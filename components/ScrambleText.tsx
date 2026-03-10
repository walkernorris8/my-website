"use client";

import { useState, useEffect, useRef } from "react";

const CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

interface ScrambleTextProps {
  text: string;
  className?: string;
  /** ms before scramble starts after entering viewport */
  delay?: number;
  /** total scramble duration in ms */
  duration?: number;
}

export default function ScrambleText({
  text,
  className = "",
  delay = 0,
  duration = 900,
}: ScrambleTextProps) {
  const [displayed, setDisplayed] = useState(text);
  const ref = useRef<HTMLSpanElement>(null);
  const startedRef = useRef(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting || startedRef.current) return;
        startedRef.current = true;
        observer.disconnect();

        setTimeout(() => {
          const start = performance.now();
          const chars = text.split("");

          const tick = (now: number) => {
            const progress = Math.min((now - start) / duration, 1);
            setDisplayed(
              chars
                .map((char, i) => {
                  if (char === " ") return " ";
                  // Each character resolves based on its position + overall progress
                  const charThreshold = (i / chars.length) * 0.8;
                  if (progress >= charThreshold + 0.2) return char;
                  if (progress < charThreshold) {
                    return CHARS[Math.floor(Math.random() * CHARS.length)];
                  }
                  // In transition: mix random + real
                  const localProgress = (progress - charThreshold) / 0.2;
                  return Math.random() < localProgress
                    ? char
                    : CHARS[Math.floor(Math.random() * CHARS.length)];
                })
                .join("")
            );
            if (progress < 1) requestAnimationFrame(tick);
            else setDisplayed(text);
          };
          requestAnimationFrame(tick);
        }, delay);
      },
      { threshold: 0.3 }
    );
    observer.observe(el);
    return () => observer.disconnect();
  }, [text, delay, duration]);

  return (
    <span ref={ref} className={`font-mono tracking-tight ${className}`}>
      {displayed}
    </span>
  );
}
