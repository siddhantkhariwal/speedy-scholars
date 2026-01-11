"use client"

import React, { useState } from 'react';
import { Phone, Mail, MapPin, Clock, Send, MessageCircle, CheckCircle } from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    childAge: '',
    message: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    // For now, we'll just simulate a submission
    // Later, you can connect this to an email service like EmailJS, Formspree, or your own backend
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Open WhatsApp with pre-filled message
    const message = `Hi, I'm ${formData.name}. I'm interested in abacus classes for my ${formData.childAge} year old child. ${formData.message}`;
    const whatsappUrl = `https://wa.me/919352646671?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');

    setIsSubmitting(false);
    setIsSubmitted(true);

    // Reset form after 3 seconds
    setTimeout(() => {
      setIsSubmitted(false);
      setFormData({ name: '', email: '', phone: '', childAge: '', message: '' });
    }, 3000);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

  return (
    <div className="min-h-screen bg-[#FFF8E7]">
      {/* Navigation */}
      <nav className="bg-[#8B6F47] py-4 px-4 md:px-8 lg:px-16">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <Link href="/" className="flex items-center space-x-3">
            <Image src="/images/logo.png" alt="Speedy Scholars Logo" width={60} height={60} className="h-14 w-14" />
            <span className="text-xl font-bold text-white">Speedy Scholars</span>
          </Link>
          <Link href="/" className="text-white hover:text-[#FFD7BA] transition">
            Back to Home
          </Link>
        </div>
      </nav>

      {/* Hero Header */}
      <header className="bg-gradient-to-br from-[#8B6F47] to-[#6B5335] py-16 px-4 md:px-8 lg:px-16 text-white text-center">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">Get In Touch</h1>
        <p className="text-xl opacity-90 max-w-2xl mx-auto">
          Have questions about our abacus classes? We&apos;d love to hear from you. Reach out and let&apos;s discuss how we can help your child excel.
        </p>
      </header>

      <main className="py-16 px-4 md:px-8 lg:px-16">
        <div className="max-w-6xl mx-auto">
          <div className="grid lg:grid-cols-2 gap-12">
            {/* Contact Information */}
            <div>
              <h2 className="text-3xl font-bold text-[#8B6F47] mb-8">Contact Information</h2>

              <div className="space-y-6">
                {/* Phone */}
                <div className="flex items-start space-x-4 p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition">
                  <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center flex-shrink-0">
                    <Phone className="w-7 h-7 text-white" />
                  </div>
                  <div>
                    <h3 className="font-bold text-[#8B6F47] text-lg mb-1">Call Us</h3>
                    <a href="tel:+919352646671" className="text-gray-700 hover:text-[#8B6F47] transition text-lg">
                      +91 9352646671
                    </a>
                    <p className="text-gray-500 text-sm mt-1">Mon-Sat, 9 AM - 7 PM IST</p>
                  </div>
                </div>

                {/* WhatsApp */}
                <a
                  href="https://wa.me/919352646671?text=Hi%2C%20I'm%20interested%20in%20abacus%20classes%20for%20my%20child."
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-start space-x-4 p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition group"
                >
                  <div className="w-14 h-14 bg-[#25D366] rounded-full flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition">
                    <MessageCircle className="w-7 h-7 text-white" />
                  </div>
                  <div>
                    <h3 className="font-bold text-[#8B6F47] text-lg mb-1">WhatsApp</h3>
                    <p className="text-gray-700 text-lg">Chat with us instantly</p>
                    <p className="text-green-600 text-sm mt-1 font-medium">Click to start chatting</p>
                  </div>
                </a>

                {/* Email */}
                <div className="flex items-start space-x-4 p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition">
                  <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center flex-shrink-0">
                    <Mail className="w-7 h-7 text-white" />
                  </div>
                  <div>
                    <h3 className="font-bold text-[#8B6F47] text-lg mb-1">Email Us</h3>
                    <a href="mailto:nidhikhariwal2012@gmail.com" className="text-gray-700 hover:text-[#8B6F47] transition text-lg">
                      nidhikhariwal2012@gmail.com
                    </a>
                    <p className="text-gray-500 text-sm mt-1">We reply within 24 hours</p>
                  </div>
                </div>

                {/* Location */}
                <div className="flex items-start space-x-4 p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition">
                  <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center flex-shrink-0">
                    <MapPin className="w-7 h-7 text-white" />
                  </div>
                  <div>
                    <h3 className="font-bold text-[#8B6F47] text-lg mb-1">Location</h3>
                    <p className="text-gray-700 text-lg">Online Classes Worldwide</p>
                    <p className="text-gray-500 text-sm mt-1">Learn from anywhere!</p>
                  </div>
                </div>

                {/* Class Timings */}
                <div className="flex items-start space-x-4 p-6 bg-white rounded-2xl shadow-lg hover:shadow-xl transition">
                  <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center flex-shrink-0">
                    <Clock className="w-7 h-7 text-white" />
                  </div>
                  <div>
                    <h3 className="font-bold text-[#8B6F47] text-lg mb-1">Class Timings</h3>
                    <p className="text-gray-700">Flexible scheduling available</p>
                    <p className="text-gray-500 text-sm mt-1">We accommodate different time zones</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Contact Form */}
            <div>
              <h2 className="text-3xl font-bold text-[#8B6F47] mb-8">Send Us a Message</h2>

              <form onSubmit={handleSubmit} className="bg-white p-8 rounded-2xl shadow-xl">
                {isSubmitted ? (
                  <div className="text-center py-12">
                    <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
                      <CheckCircle className="w-10 h-10 text-green-600" />
                    </div>
                    <h3 className="text-2xl font-bold text-[#8B6F47] mb-2">Message Sent!</h3>
                    <p className="text-gray-600">We&apos;ll get back to you soon. Check WhatsApp for instant response!</p>
                  </div>
                ) : (
                  <>
                    <div className="space-y-6">
                      {/* Name */}
                      <div>
                        <label htmlFor="name" className="block text-sm font-semibold text-[#8B6F47] mb-2">
                          Your Name *
                        </label>
                        <input
                          type="text"
                          id="name"
                          name="name"
                          value={formData.name}
                          onChange={handleChange}
                          required
                          className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-[#8B6F47] focus:outline-none transition"
                          placeholder="Enter your name"
                        />
                      </div>

                      {/* Email */}
                      <div>
                        <label htmlFor="email" className="block text-sm font-semibold text-[#8B6F47] mb-2">
                          Email Address *
                        </label>
                        <input
                          type="email"
                          id="email"
                          name="email"
                          value={formData.email}
                          onChange={handleChange}
                          required
                          className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-[#8B6F47] focus:outline-none transition"
                          placeholder="your@email.com"
                        />
                      </div>

                      {/* Phone */}
                      <div>
                        <label htmlFor="phone" className="block text-sm font-semibold text-[#8B6F47] mb-2">
                          Phone Number
                        </label>
                        <input
                          type="tel"
                          id="phone"
                          name="phone"
                          value={formData.phone}
                          onChange={handleChange}
                          className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-[#8B6F47] focus:outline-none transition"
                          placeholder="+1 234 567 8900"
                        />
                      </div>

                      {/* Child's Age */}
                      <div>
                        <label htmlFor="childAge" className="block text-sm font-semibold text-[#8B6F47] mb-2">
                          Child&apos;s Age *
                        </label>
                        <select
                          id="childAge"
                          name="childAge"
                          value={formData.childAge}
                          onChange={handleChange}
                          required
                          className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-[#8B6F47] focus:outline-none transition bg-white"
                        >
                          <option value="">Select age group</option>
                          <option value="4-5">4-5 years</option>
                          <option value="6-7">6-7 years</option>
                          <option value="8-9">8-9 years</option>
                          <option value="10-12">10-12 years</option>
                          <option value="13+">13+ years</option>
                        </select>
                      </div>

                      {/* Message */}
                      <div>
                        <label htmlFor="message" className="block text-sm font-semibold text-[#8B6F47] mb-2">
                          Your Message
                        </label>
                        <textarea
                          id="message"
                          name="message"
                          value={formData.message}
                          onChange={handleChange}
                          rows={4}
                          className="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-[#8B6F47] focus:outline-none transition resize-none"
                          placeholder="Tell us about your requirements or any questions you have..."
                        />
                      </div>
                    </div>

                    {/* Submit Button */}
                    <button
                      type="submit"
                      disabled={isSubmitting}
                      className="w-full mt-8 bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white py-4 rounded-xl font-semibold hover:shadow-xl transition transform hover:scale-[1.02] disabled:opacity-70 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                    >
                      {isSubmitting ? (
                        <>
                          <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                          Sending...
                        </>
                      ) : (
                        <>
                          <Send className="w-5 h-5" />
                          Send Message
                        </>
                      )}
                    </button>

                    <p className="text-center text-gray-500 text-sm mt-4">
                      Or chat directly on{' '}
                      <a
                        href="https://wa.me/919352646671"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-green-600 font-semibold hover:underline"
                      >
                        WhatsApp
                      </a>{' '}
                      for instant response!
                    </p>
                  </>
                )}
              </form>
            </div>
          </div>

          {/* FAQ Section */}
          <section className="mt-20">
            <h2 className="text-3xl font-bold text-[#8B6F47] mb-8 text-center">Frequently Asked Questions</h2>

            <div className="grid md:grid-cols-2 gap-6">
              {[
                {
                  q: "What age group is best for starting abacus?",
                  a: "Children can start learning abacus from age 4-5. The ideal age range is 4-14 years when the brain is most receptive to developing new neural pathways."
                },
                {
                  q: "How long does it take to see results?",
                  a: "Most parents notice improvement in their child's calculation speed and confidence within 2-3 months of regular practice. Complete mastery typically takes 2-3 years."
                },
                {
                  q: "What platform do you use for online classes?",
                  a: "We conduct classes via Zoom or Google Meet, whichever is convenient for you. All you need is a stable internet connection and a device with a camera."
                },
                {
                  q: "Is there a free trial available?",
                  a: "Yes! We offer a FREE 45-minute demo class so you can experience our teaching methodology firsthand before making any commitment."
                }
              ].map((faq, idx) => (
                <div key={idx} className="bg-white p-6 rounded-2xl shadow-lg">
                  <h3 className="font-bold text-[#8B6F47] mb-2">{faq.q}</h3>
                  <p className="text-gray-600">{faq.a}</p>
                </div>
              ))}
            </div>
          </section>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-[#8B6F47] text-white py-8 px-4 md:px-8 lg:px-16 text-center">
        <p>&copy; 2025 Speedy Scholars. All rights reserved.</p>
        <Link href="/" className="text-[#FFD7BA] hover:underline mt-2 inline-block">
          Back to Home
        </Link>
      </footer>

      {/* WhatsApp Floating Button */}
      <a
        href="https://wa.me/919352646671?text=Hi%2C%20I'm%20interested%20in%20abacus%20classes%20for%20my%20child."
        target="_blank"
        rel="noopener noreferrer"
        className="fixed bottom-6 right-6 z-50 bg-[#25D366] hover:bg-[#128C7E] text-white p-4 rounded-full shadow-2xl transition-all duration-300 hover:scale-110"
        aria-label="Chat on WhatsApp"
      >
        <svg
          className="w-7 h-7"
          fill="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
      </a>
    </div>
  );
}
