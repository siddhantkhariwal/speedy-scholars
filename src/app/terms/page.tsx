"use client"

import React from 'react';
import Link from 'next/link';
import { ArrowLeft, FileText, CheckCircle, XCircle, AlertCircle, Scale } from 'lucide-react';

export default function TermsOfServicePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-stone-50 to-stone-100">
      {/* Header */}
      <header className="bg-white shadow-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-[#8B6F47] hover:text-[#6B5335] transition-colors"
          >
            <ArrowLeft className="w-5 h-5" />
            <span className="font-semibold">Back to Home</span>
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="bg-gradient-to-br from-[#8B6F47] to-[#6B5335] text-white py-16">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-4 mb-6">
            <div className="w-16 h-16 bg-white/20 rounded-2xl flex items-center justify-center">
              <FileText className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-4xl md:text-5xl font-bold">Terms of Service</h1>
              <p className="text-white/80 mt-2">Last updated: January 28, 2026</p>
            </div>
          </div>
          <p className="text-xl text-white/90 max-w-3xl">
            Please read these Terms of Service carefully before using Speedy Scholars&apos; services.
          </p>
        </div>
      </section>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="bg-white rounded-3xl shadow-xl p-8 md:p-12">
          {/* Introduction */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Agreement to Terms</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Welcome to Speedy Scholars. These Terms of Service (&quot;Terms&quot;) govern your use of our website <a href="https://www.speedyscholars.com" className="text-[#8B6F47] hover:underline">www.speedyscholars.com</a> and online abacus classes provided by Speedy Scholars, operated by Nidhi Khariwal.
            </p>
            <p className="text-gray-600 leading-relaxed">
              By accessing or using our services, you agree to be bound by these Terms. If you disagree with any part of these terms, you may not access our services.
            </p>
          </section>

          {/* Services */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <CheckCircle className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Our Services</h2>
            </div>
            <p className="text-gray-600 leading-relaxed mb-4">
              Speedy Scholars provides online abacus education services, including:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>One-on-one online abacus classes via video conferencing</li>
              <li>Free 30-minute demo classes</li>
              <li>Regular subscription-based classes</li>
              <li>Class packages (10-class packs)</li>
              <li>Educational materials and resources</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              All classes are conducted by Nidhi Khariwal, a certified instructor with 20+ years of experience and 2000+ students worldwide.
            </p>
          </section>

          {/* Registration */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Registration and Account</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              To access our services, you must:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Be a parent or legal guardian of a child aged 5-14</li>
              <li>Provide accurate and complete information during booking</li>
              <li>Maintain the confidentiality of your booking details</li>
              <li>Notify us immediately of any unauthorized use</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              You are responsible for all activities that occur under your account.
            </p>
          </section>

          {/* Pricing and Payment */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Scale className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Pricing and Payment</h2>
            </div>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Current Pricing</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2 mb-6">
              <li><strong>Free Demo Class:</strong> 30 minutes, no payment required</li>
              <li><strong>Single Class:</strong> ₹1,600 / $20 / £15 / A$30 per 45-minute class</li>
              <li><strong>10-Class Pack:</strong> ₹12,500 / $150 / £120 / A$230 (discounted rate)</li>
            </ul>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Payment Terms</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Payment is due before or at the time of class booking</li>
              <li>We accept various payment methods (bank transfer, UPI, international payments)</li>
              <li>All prices are subject to change with 30 days&apos; notice</li>
              <li>Prices are displayed in multiple currencies for convenience</li>
              <li>Payment confirms your acceptance of these Terms</li>
            </ul>
          </section>

          {/* Cancellation and Refund */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <XCircle className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Cancellation and Refund Policy</h2>
            </div>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">By Students/Parents</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2 mb-6">
              <li><strong>Free Demo:</strong> Can be cancelled or rescheduled anytime before the class</li>
              <li><strong>Paid Classes:</strong> Must cancel at least 24 hours before scheduled time for full refund</li>
              <li><strong>Late Cancellations:</strong> Cancellations within 24 hours are non-refundable</li>
              <li><strong>No-Show:</strong> Missing a class without notice is non-refundable</li>
              <li><strong>Class Packs:</strong> Unused classes can be refunded within 30 days of purchase</li>
            </ul>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">By Speedy Scholars</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>We reserve the right to cancel classes due to unforeseen circumstances</li>
              <li>In case of cancellation by us, you will receive full refund or rescheduling option</li>
              <li>Technical issues on our end will result in free makeup class</li>
            </ul>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Refund Process</h3>
            <p className="text-gray-600 leading-relaxed mb-3">
              Approved refunds will be processed within 7-10 business days to the original payment method.
            </p>
          </section>

          {/* Class Conduct */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <AlertCircle className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Class Conduct and Expectations</h2>
            </div>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Student Responsibilities</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2 mb-6">
              <li>Attend classes on time with necessary materials (abacus, notebook, pen)</li>
              <li>Maintain a quiet, distraction-free learning environment</li>
              <li>Complete assigned homework and practice regularly</li>
              <li>Treat the instructor with respect and courtesy</li>
              <li>Have a stable internet connection and functioning device</li>
            </ul>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Parent/Guardian Responsibilities</h3>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Ensure child attends classes regularly and on time</li>
              <li>Provide necessary learning materials</li>
              <li>Monitor child&apos;s progress and practice</li>
              <li>Communicate any concerns or issues promptly</li>
              <li>Ensure payment is made on time</li>
            </ul>
          </section>

          {/* Technical Requirements */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Technical Requirements</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              To participate in online classes, you must have:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Stable internet connection (minimum 2 Mbps)</li>
              <li>Computer, laptop, or tablet with camera and microphone</li>
              <li>Video conferencing software (as specified by instructor)</li>
              <li>Quiet space for learning</li>
              <li>Physical abacus tool (can be purchased separately)</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              We are not responsible for technical issues on the student&apos;s end. However, we will work with you to reschedule if there are technical problems during the class.
            </p>
          </section>

          {/* Intellectual Property */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Intellectual Property</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              All content provided during classes, including but not limited to:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2 mb-4">
              <li>Teaching materials and worksheets</li>
              <li>Video recordings and presentations</li>
              <li>Proprietary teaching methods</li>
              <li>Website content and design</li>
            </ul>
            <p className="text-gray-600 leading-relaxed">
              remain the intellectual property of Speedy Scholars and Nidhi Khariwal. You may not reproduce, distribute, or create derivative works without explicit written permission.
            </p>
          </section>

          {/* Recording Policy */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Recording and Privacy</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Classes may be recorded for quality assurance and educational purposes. By participating in classes, you consent to:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Recording of video and audio during classes</li>
              <li>Use of recordings for internal training purposes</li>
              <li>Storage of class recordings securely</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              Students and parents may not record classes without prior written consent. Unauthorized recording or distribution of class materials is strictly prohibited.
            </p>
          </section>

          {/* Liability */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Limitation of Liability</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Speedy Scholars and its instructors shall not be liable for:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Student&apos;s academic performance or exam results</li>
              <li>Technical issues or internet connectivity problems</li>
              <li>Indirect, incidental, or consequential damages</li>
              <li>Loss of data or materials</li>
              <li>Third-party actions or services (e.g., Calendly, payment processors)</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              Our total liability for any claim arising from these Terms shall not exceed the amount paid for the specific class or service in question.
            </p>
          </section>

          {/* Termination */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Termination</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              We reserve the right to suspend or terminate your access to our services if you:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Violate these Terms of Service</li>
              <li>Provide false or misleading information</li>
              <li>Engage in abusive or inappropriate behavior</li>
              <li>Fail to make required payments</li>
              <li>Misuse our services or materials</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              Upon termination, any outstanding payments become immediately due, and unused class credits may be forfeited.
            </p>
          </section>

          {/* Dispute Resolution */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Dispute Resolution</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              In the event of any dispute or claim arising from these Terms or our services:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>We encourage direct communication to resolve issues amicably</li>
              <li>Contact us at <a href="mailto:nidhikhariwal2012@gmail.com" className="text-[#8B6F47] hover:underline">nidhikhariwal2012@gmail.com</a></li>
              <li>We will attempt to resolve disputes within 14 business days</li>
              <li>If unresolved, disputes shall be governed by Indian law (or applicable jurisdiction)</li>
            </ul>
          </section>

          {/* Changes to Terms */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Changes to Terms</h2>
            <p className="text-gray-600 leading-relaxed">
              We reserve the right to modify these Terms at any time. We will notify users of any material changes via email or website notice at least 30 days before changes take effect. Continued use of our services after changes constitutes acceptance of modified Terms.
            </p>
          </section>

          {/* Miscellaneous */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Miscellaneous</h2>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Entire Agreement</h3>
            <p className="text-gray-600 leading-relaxed mb-4">
              These Terms constitute the entire agreement between you and Speedy Scholars regarding use of our services.
            </p>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Severability</h3>
            <p className="text-gray-600 leading-relaxed mb-4">
              If any provision of these Terms is found to be unenforceable, the remaining provisions will remain in full effect.
            </p>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Waiver</h3>
            <p className="text-gray-600 leading-relaxed">
              Failure to enforce any provision of these Terms shall not constitute a waiver of that provision.
            </p>
          </section>

          {/* Contact */}
          <section className="bg-gradient-to-br from-stone-50 to-stone-100 p-8 rounded-2xl">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Contact Us</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              If you have any questions about these Terms of Service, please contact us:
            </p>
            <div className="space-y-2 text-gray-600">
              <p><strong>Email:</strong> <a href="mailto:nidhikhariwal2012@gmail.com" className="text-[#8B6F47] hover:underline">nidhikhariwal2012@gmail.com</a></p>
              <p><strong>Phone:</strong> <a href="tel:+919929322999" className="text-[#8B6F47] hover:underline">+91 99293 22999</a></p>
              <p><strong>Website:</strong> <a href="https://www.speedyscholars.com" className="text-[#8B6F47] hover:underline">www.speedyscholars.com</a></p>
              <p><strong>Business Name:</strong> Speedy Scholars</p>
              <p><strong>Founder:</strong> Nidhi Khariwal</p>
            </div>
          </section>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gradient-to-br from-[#5A4830] to-[#3D3020] text-white py-8">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-white/80">
            © 2026 Speedy Scholars. All rights reserved.
          </p>
          <div className="flex justify-center gap-6 mt-4">
            <Link href="/privacy" className="text-white/80 hover:text-white transition-colors">
              Privacy Policy
            </Link>
            <Link href="/terms" className="text-white/80 hover:text-white transition-colors">
              Terms of Service
            </Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
