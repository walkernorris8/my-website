"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Plus, Minus } from "lucide-react";

interface FaqItem {
  q: string;
  a: string;
}

interface FaqAccordionProps {
  items: FaqItem[];
}

export default function FaqAccordion({ items }: FaqAccordionProps) {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <div className="flex flex-col gap-3">
      {items.map((item, i) => (
        <div
          key={i}
          className={`border rounded-2xl overflow-hidden transition-colors duration-200 ${
            open === i ? "border-blue-200 bg-blue-50/50" : "border-gray-200 bg-gray-50"
          }`}
        >
          <button
            className="w-full flex items-center justify-between gap-4 px-6 py-5 text-left"
            onClick={() => setOpen(open === i ? null : i)}
          >
            <span className="font-semibold text-gray-900 text-sm md:text-base">
              {item.q}
            </span>
            <span className={`shrink-0 w-6 h-6 rounded-full flex items-center justify-center transition-colors duration-200 ${
              open === i ? "bg-blue-600 text-white" : "bg-gray-200 text-gray-500"
            }`}>
              {open === i ? <Minus className="w-3.5 h-3.5" /> : <Plus className="w-3.5 h-3.5" />}
            </span>
          </button>

          <AnimatePresence initial={false}>
            {open === i && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: "auto", opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.25, ease: [0.25, 0.1, 0.25, 1] }}
              >
                <div className="px-6 pb-5 text-gray-600 text-sm leading-relaxed border-t border-blue-100">
                  <div className="pt-4">{item.a}</div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      ))}
    </div>
  );
}
