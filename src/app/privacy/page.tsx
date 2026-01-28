"use client"

import React from 'react';
import Link from 'next/link';
import { ArrowLeft, Shield, Lock, Eye, Database, Users, Globe } from 'lucide-react';

export default function PrivacyPolicyPage() {
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
              <Shield className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-4xl md:text-5xl font-bold">Privacy Policy</h1>
              <p className="text-white/80 mt-2">Last updated: January 28, 2026</p>
            </div>
          </div>
          <p className="text-xl text-white/90 max-w-3xl">
            At Speedy Scholars, we are committed to protecting your privacy and ensuring the security of your personal information.
          </p>
        </div>
      </section>

      {/* Content */}
      <main className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="bg-white rounded-3xl shadow-xl p-8 md:p-12">
          {/* Introduction */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Introduction</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Welcome to Speedy Scholars. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website <a href="https://www.speedyscholars.com" className="text-[#8B6F47] hover:underline">www.speedyscholars.com</a> and use our services.
            </p>
            <p className="text-gray-600 leading-relaxed">
              By using our services, you agree to the collection and use of information in accordance with this policy. If you do not agree with our policies and practices, please do not use our services.
            </p>
          </section>

          {/* Information We Collect */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Database className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Information We Collect</h2>
            </div>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Personal Information</h3>
            <p className="text-gray-600 leading-relaxed mb-3">
              We may collect personal information that you voluntarily provide to us when you:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2 mb-6">
              <li>Book a demo class through our Calendly integration</li>
              <li>Contact us via email, phone, or WhatsApp</li>
              <li>Subscribe to our newsletter or communications</li>
              <li>Register for our abacus classes</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mb-4">
              This information may include:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Parent/Guardian name and contact information</li>
              <li>Student name and age</li>
              <li>Email address and phone number</li>
              <li>Country/location for currency detection</li>
              <li>Payment information (processed securely through third-party providers)</li>
            </ul>

            <h3 className="text-xl font-bold text-gray-900 mt-6 mb-3">Automatically Collected Information</h3>
            <p className="text-gray-600 leading-relaxed mb-3">
              When you visit our website, we automatically collect certain information about your device, including:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>IP address and general location</li>
              <li>Browser type and version</li>
              <li>Pages visited and time spent on pages</li>
              <li>Referring website addresses</li>
              <li>Device type and operating system</li>
            </ul>
          </section>

          {/* How We Use Your Information */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Eye className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">How We Use Your Information</h2>
            </div>
            <p className="text-gray-600 leading-relaxed mb-4">
              We use the information we collect for the following purposes:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>To provide and maintain our educational services</li>
              <li>To schedule and conduct demo classes and regular classes</li>
              <li>To communicate with you about your classes, payments, and updates</li>
              <li>To process payments and manage subscriptions</li>
              <li>To improve our website and services</li>
              <li>To analyze usage trends and optimize user experience</li>
              <li>To send promotional communications (with your consent)</li>
              <li>To comply with legal obligations</li>
            </ul>
          </section>

          {/* Third-Party Services */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Users className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Third-Party Services</h2>
            </div>
            <p className="text-gray-600 leading-relaxed mb-4">
              We use the following third-party services that may collect information:
            </p>

            <div className="space-y-4">
              <div className="bg-stone-50 p-4 rounded-xl">
                <h4 className="font-bold text-gray-900 mb-2">Google Analytics</h4>
                <p className="text-gray-600 text-sm">
                  We use Google Analytics to analyze website traffic and usage patterns. Google Analytics uses cookies to collect anonymous data.
                </p>
              </div>

              <div className="bg-stone-50 p-4 rounded-xl">
                <h4 className="font-bold text-gray-900 mb-2">Calendly</h4>
                <p className="text-gray-600 text-sm">
                  We use Calendly for scheduling demo classes. When you book a class, Calendly collects your name, email, and selected time slot.
                </p>
              </div>

              <div className="bg-stone-50 p-4 rounded-xl">
                <h4 className="font-bold text-gray-900 mb-2">Vercel (Hosting)</h4>
                <p className="text-gray-600 text-sm">
                  Our website is hosted on Vercel, which may collect technical data for security and performance monitoring.
                </p>
              </div>
            </div>
          </section>

          {/* Data Security */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Lock className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Data Security</h2>
            </div>
            <p className="text-gray-600 leading-relaxed mb-4">
              We implement appropriate technical and organizational measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction. These measures include:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>SSL/TLS encryption for data transmission</li>
              <li>Secure servers and databases</li>
              <li>Regular security audits and updates</li>
              <li>Limited access to personal information</li>
              <li>Secure payment processing through trusted providers</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              However, no method of transmission over the internet or electronic storage is 100% secure. While we strive to protect your information, we cannot guarantee its absolute security.
            </p>
          </section>

          {/* Your Rights */}
          <section className="mb-12">
            <div className="flex items-center gap-3 mb-4">
              <Globe className="w-6 h-6 text-[#8B6F47]" />
              <h2 className="text-3xl font-bold text-gray-900">Your Privacy Rights</h2>
            </div>
            <p className="text-gray-600 leading-relaxed mb-4">
              Depending on your location, you may have the following rights regarding your personal information:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li><strong>Access:</strong> Request a copy of the personal information we hold about you</li>
              <li><strong>Correction:</strong> Request correction of inaccurate or incomplete information</li>
              <li><strong>Deletion:</strong> Request deletion of your personal information</li>
              <li><strong>Restriction:</strong> Request restriction of processing your information</li>
              <li><strong>Data Portability:</strong> Request transfer of your data to another service</li>
              <li><strong>Objection:</strong> Object to processing of your information</li>
              <li><strong>Withdraw Consent:</strong> Withdraw consent for processing at any time</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              To exercise these rights, please contact us at <a href="mailto:nidhikhariwal2012@gmail.com" className="text-[#8B6F47] hover:underline">nidhikhariwal2012@gmail.com</a>
            </p>
          </section>

          {/* Children's Privacy */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Children&apos;s Privacy</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Our services are designed for children aged 5-14, but we collect personal information only from parents or legal guardians. We do not knowingly collect personal information directly from children without parental consent.
            </p>
            <p className="text-gray-600 leading-relaxed">
              Parents have the right to review, delete, or refuse further collection of their child&apos;s information. Please contact us if you believe we have inadvertently collected information from a child without proper consent.
            </p>
          </section>

          {/* Cookies */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Cookies and Tracking</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              We use cookies and similar tracking technologies to enhance your experience on our website. Cookies are small files stored on your device that help us:
            </p>
            <ul className="list-disc pl-6 text-gray-600 space-y-2">
              <li>Remember your preferences and settings</li>
              <li>Understand how you use our website</li>
              <li>Improve website performance</li>
              <li>Provide personalized content</li>
            </ul>
            <p className="text-gray-600 leading-relaxed mt-4">
              You can control cookies through your browser settings. However, disabling cookies may affect your experience on our website.
            </p>
          </section>

          {/* International Data Transfers */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">International Data Transfers</h2>
            <p className="text-gray-600 leading-relaxed">
              We serve students globally (USA, UK, Australia, India, and other countries). Your information may be transferred to and processed in countries other than your own. We ensure appropriate safeguards are in place to protect your information in accordance with this Privacy Policy and applicable laws.
            </p>
          </section>

          {/* Changes to Policy */}
          <section className="mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Changes to This Privacy Policy</h2>
            <p className="text-gray-600 leading-relaxed">
              We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the &quot;Last updated&quot; date. We encourage you to review this Privacy Policy periodically for any changes.
            </p>
          </section>

          {/* Contact */}
          <section className="bg-gradient-to-br from-stone-50 to-stone-100 p-8 rounded-2xl">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Contact Us</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              If you have any questions about this Privacy Policy or our data practices, please contact us:
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
