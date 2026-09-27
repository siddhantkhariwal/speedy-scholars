"use client";

import { useEffect, useRef } from "react";
import Cal, { getCalApi } from "@calcom/embed-react";

export const CAL_LINK = "nidhi-khariwal/free-demo-30-min";
export const CAL_NAMESPACE = "demo";
const CAL_CONFIG = { layout: "month_view", theme: "light" } as const;

/**
 * Fires `book_demo_complete` once per completed booking.
 *
 * Cal.com's free plan has no "redirect on booking", so instead we listen for
 * the embed's `bookingSuccessfulV2` event. That event carries the booking uid,
 * which we use to make sure a booking is only ever counted once. This is the
 * event to mark as a key event in GA4. `book_demo_click` only means the
 * calendar was opened.
 */
function trackBookingComplete(uid: string | undefined) {
  const key = `ss_booking_${uid ?? "unknown"}`;
  try {
    if (uid && sessionStorage.getItem(key)) return;
    if (uid) sessionStorage.setItem(key, "1");
  } catch {
    /* storage blocked, track anyway */
  }
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const w = window as any;
  w.dataLayer = w.dataLayer || [];
  // GA loads lazily, so queue through dataLayer the same way gtag() does.
  // eslint-disable-next-line prefer-rest-params
  const gtag = w.gtag || function () { w.dataLayer.push(arguments); };
  gtag("event", "book_demo_complete", { event_category: "conversion", method: "cal.com" });
}

/** Loads the Cal.com embed API once and listens for completed bookings. */
export function useCalBooking(onReady?: () => void) {
  // A ref, so a new onReady function on re-render doesn't re-register listeners.
  const onReadyRef = useRef(onReady);
  onReadyRef.current = onReady;

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const cal = await getCalApi({ namespace: CAL_NAMESPACE });
      if (cancelled) return;
      cal("ui", { theme: "light", hideEventTypeDetails: false, layout: "month_view" });
      cal("on", {
        action: "bookingSuccessfulV2",
        callback: (e) => trackBookingComplete(e.detail.data.uid),
      });
      cal("on", { action: "linkReady", callback: () => onReadyRef.current?.() });
    })();
    return () => {
      cancelled = true;
    };
  }, []);
}

/** The booking calendar rendered inline, used inside the homepage modal. */
export function CalInline({ onReady }: { onReady?: () => void }) {
  useCalBooking(onReady);
  return (
    <Cal
      namespace={CAL_NAMESPACE}
      calLink={CAL_LINK}
      config={CAL_CONFIG}
      style={{ width: "100%", height: "100%", overflow: "auto" }}
    />
  );
}

/**
 * Attributes that turn any button into a Cal.com booking popup on the same
 * page. The page must also call useCalBooking() once.
 */
export const calPopupAttrs = {
  "data-cal-link": CAL_LINK,
  "data-cal-namespace": CAL_NAMESPACE,
  "data-cal-config": JSON.stringify(CAL_CONFIG),
};
