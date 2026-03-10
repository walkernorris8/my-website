"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, Calendar } from "lucide-react";

interface Post {
  title: string;
  slug: { current: string };
  publishedAt: string;
  excerpt: string;
}

const QUERY = encodeURIComponent(
  `*[_type == "post"] | order(publishedAt desc) [0..2] { title, slug, publishedAt, excerpt }`
);
const SANITY_URL = `https://g1hic8ei.apicdn.sanity.io/v2021-10-21/data/query/production?query=${QUERY}`;

function formatDate(iso: string) {
  return new Date(iso).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

export default function LatestPosts() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(SANITY_URL)
      .then((r) => r.json())
      .then((data) => {
        setPosts(data.result ?? []);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (!loading && posts.length === 0) return null;

  return (
    <section className="py-24 px-6 bg-white border-t border-gray-100">
      <div className="max-w-6xl mx-auto">
        <motion.div
          className="flex items-end justify-between mb-12"
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
        >
          <div>
            <p className="text-blue-600 text-sm font-semibold uppercase tracking-widest mb-2">
              From the Blog
            </p>
            <h2 className="text-3xl md:text-4xl font-bold">Latest Insights</h2>
          </div>
          <Link
            href="/blog"
            className="hidden sm:inline-flex items-center gap-1.5 text-sm text-gray-500 hover:text-blue-600 font-medium transition-colors group"
          >
            View all posts
            <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
          </Link>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {loading
            ? Array.from({ length: 3 }).map((_, i) => (
                <div
                  key={i}
                  className="rounded-2xl border border-gray-100 bg-gray-50 p-6 animate-pulse"
                >
                  <div className="h-3 bg-gray-200 rounded w-24 mb-4" />
                  <div className="h-5 bg-gray-200 rounded w-full mb-2" />
                  <div className="h-5 bg-gray-200 rounded w-3/4 mb-4" />
                  <div className="h-3 bg-gray-200 rounded w-full mb-1" />
                  <div className="h-3 bg-gray-200 rounded w-5/6" />
                </div>
              ))
            : posts.map((post, i) => (
                <motion.div
                  key={post.slug.current}
                  initial={{ opacity: 0, y: 28 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.1 }}
                >
                  <Link
                    href={`/blog/${post.slug.current}`}
                    className="group block h-full rounded-2xl border border-gray-100 bg-gray-50 hover:border-blue-200 hover:bg-blue-50/40 p-6 transition-all duration-300"
                  >
                    <div className="flex items-center gap-1.5 text-xs text-gray-400 mb-4">
                      <Calendar className="w-3.5 h-3.5" />
                      {formatDate(post.publishedAt)}
                    </div>
                    <h3 className="font-bold text-gray-900 leading-snug mb-3 group-hover:text-blue-600 transition-colors">
                      {post.title}
                    </h3>
                    {post.excerpt && (
                      <p className="text-gray-500 text-sm leading-relaxed line-clamp-3">
                        {post.excerpt}
                      </p>
                    )}
                    <div className="mt-4 flex items-center gap-1 text-blue-600 text-xs font-semibold opacity-0 group-hover:opacity-100 transition-opacity">
                      Read post <ArrowRight className="w-3 h-3" />
                    </div>
                  </Link>
                </motion.div>
              ))}
        </div>

        <div className="mt-8 text-center sm:hidden">
          <Link
            href="/blog"
            className="inline-flex items-center gap-1.5 text-sm text-gray-500 hover:text-blue-600 font-medium transition-colors"
          >
            View all posts <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </section>
  );
}
