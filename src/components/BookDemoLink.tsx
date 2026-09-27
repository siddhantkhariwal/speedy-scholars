"use client";

import React from "react";
import { calPopupAttrs, useCalBooking } from "@/components/CalBooking";

/**
 * Booking CTA for pages outside the homepage (the homepage has its own modal).
 * Opens the Cal.com booking popup on the same page, so the visitor stays on
 * the site and a completed booking fires `book_demo_complete`. The click fires
 * the same GA4 event shape as openCalendly() on the homepage, so all Book Demo
 * clicks stay in one funnel.
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
  useCalBooking();

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
    <button
      type="button"
      {...calPopupAttrs}
      onClick={handleClick}
      className={`${base} ${styles} ${className}`}
    >
      {children}
    </button>
  );
}
