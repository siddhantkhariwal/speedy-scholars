"use client";

import { useEffect } from "react";

/**
 * Fires the `book_demo_complete` GA4 event once per completed booking.
 *
 * Cal.com's "Redirect on booking" sends the booker here. When the booking was
 * made inside the homepage modal, that redirect happens inside the iframe, so
 * we lift the page into the top window and let the top-level load do the
 * tracking. Otherwise every modal booking would count twice.
 *
 * `book_demo_click` only says someone opened the calendar. This event says a
 * slot was actually taken, and it is the one to mark as a key event in GA4.
 */
export function BookingTracker() {
  useEffect(() => {
    if (window.top && window.top !== window.self) {
      window.top.location.href = window.location.pathname;
      return;
    }

    // Cal.com can forward name/email as query params. Strip them before GA
    // reads page_location, since GA must not receive personal data.
    if (window.location.search) {
      window.history.replaceState(null, "", window.location.pathname);
    }

    // Refreshing the page should not count a second booking.
    const KEY = "ss_booking_tracked_at";
    try {
      const last = Number(sessionStorage.getItem(KEY) || 0);
      if (Date.now() - last < 30 * 60 * 1000) return;
      sessionStorage.setItem(KEY, String(Date.now()));
    } catch {
      /* storage blocked, track anyway */
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const w = window as any;
    w.dataLayer = w.dataLayer || [];
    // GA loads lazily, so queue through dataLayer the same way gtag() does.
    // eslint-disable-next-line prefer-rest-params
    const gtag = w.gtag || function () { w.dataLayer.push(arguments); };
    gtag("event", "book_demo_complete", { event_category: "conversion" });
  }, []);

  return null;
}
