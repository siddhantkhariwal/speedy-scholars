"use client";

import React from "react";

const CAL_URL = "https://cal.com/nidhi-khariwal/free-demo-30-min";

/**
 * Booking CTA for pages outside the homepage (the homepage has its own modal).
 * Opens the Cal.com booking page and fires the same GA4 event shape as
 * openCalendly() on the homepage, so all Book Demo clicks stay in one funnel.
 */
export function BookDemoLink({
  location,
  children,
  variant = "primary",
  className = "",
}: {
  location: string;
  children: React.ReactNode;
  variant?: "primary" | "gold";
  className?: string;
}) {
  const base =
    "inline-flex items-center justify-center gap-2 px-8 py-4 rounded-full font-semibold text-lg transition-all shadow-lg hover:shadow-xl";
  const styles =
    variant === "gold"
      ? "bg-[#F9AE27] text-[#32173F] hover:bg-[#CA8406]"
      : "bg-[#5A2A72] text-white hover:bg-[#3F1D50]";

  const handleClick = () => {
    try {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const w = window as any;
      if (typeof window !== "undefined" && w.gtag) {
        w.gtag("event", "book_demo_click", {
          event_category: "engagement",
          event_label: location,
        });
      }
    } catch {
      /* GA not loaded */
    }
  };

  return (
    <a
      href={CAL_URL}
      target="_blank"
      rel="noopener noreferrer"
      onClick={handleClick}
      className={`${base} ${styles} ${className}`}
    >
      {children}
    </a>
  );
}
