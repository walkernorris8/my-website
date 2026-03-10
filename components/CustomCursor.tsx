"use client";

import { useEffect, useState } from "react";
import { motion, useSpring } from "framer-motion";

export default function CustomCursor() {
  const [visible, setVisible] = useState(false);
  const [hovering, setHovering] = useState(false);
  const [clicking, setClicking] = useState(false);

  // Dot: snappy, follows immediately
  const dotX = useSpring(0, { stiffness: 2000, damping: 80, mass: 0.2 });
  const dotY = useSpring(0, { stiffness: 2000, damping: 80, mass: 0.2 });

  // Ring: trails behind with spring lag
  const ringX = useSpring(0, { stiffness: 200, damping: 28, mass: 0.5 });
  const ringY = useSpring(0, { stiffness: 200, damping: 28, mass: 0.5 });

  useEffect(() => {
    const onMove = (e: MouseEvent) => {
      dotX.set(e.clientX);
      dotY.set(e.clientY);
      ringX.set(e.clientX);
      ringY.set(e.clientY);
      setVisible(true);

      const target = (e.target as HTMLElement).closest(
        'a, button, [role="button"], input, textarea, select, label, [data-cursor]'
      );
      setHovering(!!target);
    };

    const onLeave = () => setVisible(false);
    const onDown = () => setClicking(true);
    const onUp = () => setClicking(false);

    document.addEventListener("mousemove", onMove);
    document.addEventListener("mouseleave", onLeave);
    document.addEventListener("mousedown", onDown);
    document.addEventListener("mouseup", onUp);

    return () => {
      document.removeEventListener("mousemove", onMove);
      document.removeEventListener("mouseleave", onLeave);
      document.removeEventListener("mousedown", onDown);
      document.removeEventListener("mouseup", onUp);
    };
  }, [dotX, dotY, ringX, ringY]);

  return (
    <>
      {/* Dot */}
      <motion.div
        className="fixed top-0 left-0 z-[9999] pointer-events-none"
        style={{ x: dotX, y: dotY }}
        animate={{
          opacity: visible ? 1 : 0,
          scale: clicking ? 0.4 : hovering ? 0 : 1,
        }}
        transition={{ duration: 0.12 }}
      >
        <div className="w-2 h-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-blue-400" />
      </motion.div>

      {/* Ring */}
      <motion.div
        className="fixed top-0 left-0 z-[9998] pointer-events-none"
        style={{ x: ringX, y: ringY }}
        animate={{
          opacity: visible ? 1 : 0,
          scale: clicking ? 0.75 : hovering ? 1.6 : 1,
        }}
        transition={{ scale: { type: "spring", stiffness: 350, damping: 22 }, opacity: { duration: 0.15 } }}
      >
        <div
          className={`w-9 h-9 -translate-x-1/2 -translate-y-1/2 rounded-full border transition-colors duration-150 ${
            hovering
              ? "border-blue-400 bg-blue-400/12"
              : "border-white/35 bg-transparent"
          }`}
        />
      </motion.div>
    </>
  );
}
