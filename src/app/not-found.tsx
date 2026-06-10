"use client"

import React from 'react';
import Link from 'next/link';
import { Home, Search, Calculator } from 'lucide-react';

export default function NotFound() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-stone-50 to-stone-100 flex items-center justify-center px-4">
      <div className="max-w-2xl w-full text-center">
        {/* 404 Illustration */}
        <div className="mb-8 flex justify-center">
          <div className="relative">
            <div className="text-[150px] md:text-[200px] font-bold text-[#5A2A72]/10 leading-none">
              404
            </div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-24 h-24 bg-gradient-to-br from-[#5A2A72] to-[#3F1D50] rounded-full flex items-center justify-center animate-bounce">
                <Calculator className="w-12 h-12 text-white" />
              </div>
            </div>
          </div>
        </div>

        {/* Message */}
        <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Oops! Page Not Found
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Looks like this page took a wrong turn on the abacus! Let&apos;s get you back on track.
        </p>

        {/* Fun Math Fact */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-8 border-2 border-[#5A2A72]/20">
          <p className="text-sm font-semibold text-[#5A2A72] mb-2">Did you know?</p>
          <p className="text-gray-700">
            The word &quot;abacus&quot; comes from the Greek word &quot;abax,&quot; meaning &quot;calculating board.&quot;
            It&apos;s been helping people solve math problems for over 2,000 years!
          </p>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link
            href="/"
            className="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#5A2A72] to-[#3F1D50] text-white px-8 py-4 rounded-full font-semibold text-lg hover:from-[#6B3486] hover:to-[#32173F] transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-105"
          >
            <Home className="w-5 h-5" />
            Back to Home
          </Link>

          <Link
            href="/contact"
            className="inline-flex items-center justify-center gap-2 bg-white text-[#5A2A72] px-8 py-4 rounded-full font-semibold text-lg hover:bg-stone-50 transition-all duration-300 shadow-lg border-2 border-[#5A2A72]"
          >
            <Search className="w-5 h-5" />
            Contact Us
          </Link>
        </div>

        {/* Popular Links */}
        <div className="mt-12 pt-8 border-t border-gray-200">
          <p className="text-sm font-semibold text-gray-500 mb-4">POPULAR PAGES</p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/" className="text-[#5A2A72] hover:text-[#3F1D50] font-medium transition-colors">
              Home
            </Link>
            <span className="text-gray-300">•</span>
            <Link href="/about" className="text-[#5A2A72] hover:text-[#3F1D50] font-medium transition-colors">
              About
            </Link>
            <span className="text-gray-300">•</span>
            <Link href="/contact" className="text-[#5A2A72] hover:text-[#3F1D50] font-medium transition-colors">
              Contact
            </Link>
            <span className="text-gray-300">•</span>
            <Link href="/privacy" className="text-[#5A2A72] hover:text-[#3F1D50] font-medium transition-colors">
              Privacy Policy
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}