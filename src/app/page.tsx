"use client"

import React, { useState, useEffect } from 'react';
import { CheckCircle, Phone, Mail, MapPin, Star, Users, BookOpen, Brain, Clock, Award, Menu, X, Target, Lightbulb, Smile } from 'lucide-react';
import Image from 'next/image';

// Modal Component for Calendly
function CalendlyModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-50 backdrop-blur-sm">
      <div className="relative w-full max-w-4xl bg-[#FFF8E7] rounded-2xl shadow-2xl overflow-hidden">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 z-10 p-2 bg-white rounded-full hover:bg-gray-100 transition"
        >
          <X className="w-6 h-6 text-gray-700" />
        </button>
        <div className="p-8">
          <h3 className="text-3xl font-bold text-[#8B6F47] mb-4 text-center">Book Your Free Demo Class</h3>
          <p className="text-center text-gray-700 mb-6">Choose a time that works best for you</p>
          <div className="aspect-video bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-xl flex items-center justify-center">
            <div className="text-center text-white">
              <Clock className="w-16 h-16 mx-auto mb-4 opacity-80" />
              <p className="text-lg mb-2">Calendly Widget Placeholder</p>
              <p className="text-sm opacity-80">Add your Calendly embed code here</p>
              <div className="mt-4 p-4 bg-white bg-opacity-20 rounded-lg inline-block max-w-md">
                <code className="text-xs text-white break-all">
                  {`<div className="calendly-inline-widget" data-url="your-calendly-url" style={{minWidth:'320px',height:'630px'}}></div>`}
                </code>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Abacus Animation SVG Component
function AbacusAnimation() {
  return (
    <svg className="w-full h-48" viewBox="0 0 400 200">
      <g>
        {[0, 1, 2, 3, 4].map((row) => (
          <g key={row}>
            <line x1="50" y1={40 + row * 30} x2="350" y2={40 + row * 30} stroke="#A89F91" strokeWidth="4" />
            {[0, 1, 2, 3, 4, 5].map((col) => (
              <circle
                key={`${row}-${col}`}
                cx={75 + col * 50}
                cy={40 + row * 30}
                r="15"
                fill="#E8B4A0"
                stroke="#8B6F47"
                strokeWidth="2"
                className="animate-pulse"
                style={{
                  animationDelay: `${(row + col) * 0.1}s`,
                  animationDuration: '3s'
                }}
              />
            ))}
          </g>
        ))}
      </g>
    </svg>
  );
}

export default function SpeedyScholarsLanding() {
  const [isVisible, setIsVisible] = useState(false);
  const [isVideoLoaded, setIsVideoLoaded] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isCalendlyOpen, setIsCalendlyOpen] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const navLinks = [
    { href: "#about", label: "About" },
    { href: "#pricing", label: "Pricing" },
    { href: "#testimonials", label: "Testimonials" },
    { href: "#contact", label: "Contact" },
  ];

  return (
    <div className="min-h-screen bg-[#FFF8E7]">
      {/* Glass Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-white bg-opacity-10 backdrop-filter backdrop-blur-lg">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <a href="#" className="flex items-center space-x-2">
              <Image src="/images/logo.png" alt="Speedy Scholars Logo" width={64} height={64} className="h-16 w-16" />
              <span className="text-xl font-bold text-white">Speedy Scholars</span>
            </a>
            
            <div className="hidden md:flex items-center space-x-6">
              {navLinks.map((link) => (
                <a key={link.href} href={link.href} className="text-white hover:text-[#FFD7BA] transition-colors">
                  {link.label}
                </a>
              ))}
            </div>

            <div className="flex items-center space-x-4">
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="hidden sm:flex items-center bg-gradient-to-r from-[#FFD7BA] to-[#E8B4A0] text-[#8B6F47] px-6 py-2 rounded-full font-semibold hover:shadow-lg transition transform hover:scale-105"
              >
                Book Demo
                <svg className="ml-2 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
              
              <button
                onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                className="md:hidden text-white"
              >
                {isMobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
              </button>
            </div>
          </div>

          {/* Mobile Menu */}
          {isMobileMenuOpen && (
            <div className="md:hidden mt-4 pb-4 space-y-2">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="block text-white hover:text-[#FFD7BA] transition-colors py-2"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  {link.label}
                </a>
              ))}
              <button
                onClick={() => {
                  setIsCalendlyOpen(true);
                  setIsMobileMenuOpen(false);
                }}
                className="w-full bg-gradient-to-r from-[#FFD7BA] to-[#E8B4A0] text-[#8B6F47] px-6 py-3 rounded-full font-semibold mt-2"
              >
                Book Demo
              </button>
            </div>
          )}
        </div>
      </nav>

      {/* Hero Section with Video */}
      <section className="relative h-screen w-full overflow-hidden">
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute top-0 left-0 w-full h-full object-cover z-0"
          onLoadedData={() => setIsVideoLoaded(true)}
        >
          <source src="/images/abacusVideo.mp4" type="video/mp4" />
        </video>

        <div className="absolute top-0 left-0 w-full h-full bg-black opacity-50 z-[1]" />

        <div className="absolute inset-0 z-20 flex flex-col items-center justify-center text-white px-4 text-center">
          <div className="inline-block bg-gradient-to-r from-[#FFD7BA] to-[#E8B4A0] text-[#8B6F47] px-6 py-3 rounded-full text-sm font-semibold mb-6">
            ✨ New Classes Available Now
          </div>
          
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold mb-6 drop-shadow-lg">
            Unlock Your Child's
            <br />
            <span className="text-[#FFD7BA]">Mathematical Genius</span>
          </h1>
          
          <p className="text-xl md:text-2xl mb-8 max-w-2xl drop-shadow-md">
            Transform mental arithmetic into a fun adventure with our engaging abacus classes
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4">
            <button
              onClick={() => setIsCalendlyOpen(true)}
              className="bg-gradient-to-r from-[#FFD7BA] to-[#E8B4A0] text-[#8B6F47] px-8 py-4 rounded-full font-semibold hover:shadow-xl transition transform hover:scale-105"
            >
              Book Free Demo Class
            </button>
            <a
              href="#pricing"
              className="bg-white bg-opacity-20 backdrop-blur-sm text-white px-8 py-4 rounded-full font-semibold border-2 border-white hover:bg-opacity-30 transition"
            >
              View Pricing
            </a>
          </div>
        </div>

        {/* Animated Abacus Beads at Bottom */}
        <div className="absolute bottom-0 left-0 w-full h-16 flex justify-around items-end overflow-hidden">
          {[...Array(10)].map((_, index) => (
            <div
              key={index}
              className="w-4 h-16 bg-[#E8B4A0] rounded-full animate-bounce opacity-70"
              style={{
                animationDelay: `${index * 0.1}s`,
                animationDuration: '2s'
              }}
            />
          ))}
        </div>
      </section>

      {/* About Section with Real Abacus Image and Badge */}
      <section id="about" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7] relative">
        <div className="absolute top-10 right-10 bg-white px-6 py-3 rounded-full shadow-lg hidden md:block">
          <div className="flex items-center space-x-2">
            <Star className="w-5 h-5 text-yellow-500 fill-current" />
            <span className="font-bold text-[#8B6F47]">4.9/5</span>
            <span className="text-gray-600 text-sm">from parents</span>
          </div>
        </div>

        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-2 gap-12 items-center mb-16">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold mb-4 text-[#8B6F47]">
                We Are SPEEDY SCHOLARS
              </h2>
              <h3 className="text-3xl md:text-5xl font-bold mb-6 text-[#A89F91]">
                UNLOCK THE POWER OF YOUR MIND
              </h3>
              <p className="text-xl text-gray-700 mb-4">
                Precision, Speed, and Fun with Abacus
              </p>
              <p className="text-lg text-gray-700 leading-relaxed">
                At Speedy Scholars, we boost your child's mental arithmetic skills, turning
                math into a fun and engaging activity. We enhance concentration and memory,
                increasing confidence and paving the way to academic success.
              </p>
            </div>
            <div className="relative">
              <div className="rounded-3xl overflow-hidden shadow-2xl">
                <Image 
                  src="/images/abacus.jpeg" 
                  alt="Traditional Abacus" 
                  width={600} 
                  height={400}
                  className="w-full h-auto"
                />
              </div>
            </div>
          </div>

          {/* Scrabble Learning Image Section */}
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="relative order-2 md:order-1">
              <div className="rounded-3xl overflow-hidden shadow-2xl">
                <Image 
                  src="/images/learn.jpeg" 
                  alt="Learning Journey" 
                  width={600} 
                  height={400}
                  className="w-full h-auto"
                />
              </div>
            </div>
            <div className="order-1 md:order-2">
              <h3 className="text-3xl font-bold mb-6 text-[#8B6F47]">
                Begin Your Learning Journey
              </h3>
              <p className="text-lg text-gray-700 leading-relaxed mb-6">
                Every child learns at their own pace. Our personalized approach ensures that each student receives the attention and guidance they need to excel. From foundational concepts to advanced techniques, we're with you every step of the way.
              </p>
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="bg-gradient-to-r from-[#E8B4A0] to-[#D4A89C] text-white px-8 py-4 rounded-full font-semibold hover:shadow-lg transition transform hover:scale-105"
              >
                Start Learning Today
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Benefits Section with Images */}
      <section className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-[#FAF3E0] to-[#FFD7BA]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-[#8B6F47] mb-4">Why Choose Speedy Scholars?</h2>
            <p className="text-xl text-gray-700">Excellence in Every Aspect</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {/* Enhanced Mental Arithmetic */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/brain2.jpeg" 
                  alt="Brain Development" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Enhanced Mental Arithmetic</h3>
              <p className="text-gray-700">Develop lightning-fast calculation skills that last a lifetime through proven abacus methods.</p>
            </div>

            {/* Expert Instruction with Image */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/class.jpeg" 
                  alt="Expert Teaching" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Expert Instruction</h3>
              <p className="text-gray-700">Learn from Mrs. Nidhi, a passionate and experienced abacus educator dedicated to your child's success.</p>
            </div>

            {/* Proven Results */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/goal.jpeg" 
                  alt="Achievement Goals" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Proven Results</h3>
              <p className="text-gray-700">Watch confidence soar as academic success becomes the norm with measurable improvements.</p>
            </div>

            {/* Engaging Curriculum */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/imagination.jpeg" 
                  alt="Engaging Learning" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Engaging Curriculum</h3>
              <p className="text-gray-700">Fun, interactive lessons that keep children excited to learn and explore mathematics.</p>
            </div>

            {/* Flexible Online Learning */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/student.jpeg" 
                  alt="Online Learning" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Flexible Scheduling</h3>
              <p className="text-gray-700">Join classes anytime, anywhere with our convenient online sessions tailored to your schedule.</p>
            </div>

            {/* Holistic Development */}
            <div className="bg-white p-8 rounded-2xl hover:shadow-xl transition transform hover:-translate-y-2">
              <div className="mb-4 rounded-xl overflow-hidden">
                <Image 
                  src="/images/study.jpeg" 
                  alt="Student Progress" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-xl font-bold text-[#8B6F47] mb-3">Holistic Development</h3>
              <p className="text-gray-700">Boost memory, concentration, and problem-solving abilities beyond just mathematics.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-[#8B6F47] mb-4">Simple, Transparent Pricing</h2>
            <p className="text-xl text-gray-700">Choose the plan that works best for your family</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            {/* Demo Class */}
            <div className="bg-gradient-to-br from-[#C9B8A8] to-[#A89F91] border-2 border-[#8B6F47] p-8 rounded-2xl text-white shadow-xl">
              <h3 className="text-2xl font-semibold mb-2">Demo Class</h3>
              <div className="text-6xl font-bold mb-4">₹0</div>
              <p className="mb-6 opacity-90">First 45 Mins Abacus Class is on us.</p>
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="w-full bg-white text-[#8B6F47] py-3 rounded-full font-semibold hover:bg-[#FFD7BA] transition transform hover:scale-105"
              >
                Book Now
              </button>
            </div>

            {/* Pay-As-You-Go */}
            <div className="bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] border-2 border-[#8B6F47] p-8 rounded-2xl text-white shadow-xl">
              <h3 className="text-2xl font-semibold mb-2">Pay-As-You-Go</h3>
              <div className="text-6xl font-bold mb-4">₹1,600</div>
              <p className="mb-6 opacity-90">Experience flexible learning with our Single Session Pass.</p>
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="w-full bg-white text-[#8B6F47] py-3 rounded-full font-semibold hover:bg-[#FFD7BA] transition transform hover:scale-105"
              >
                Select
              </button>
              <ul className="mt-6 space-y-2 text-sm">
                <li className="flex items-start opacity-90">
                  <CheckCircle className="w-5 h-5 mr-2 flex-shrink-0" />
                  <span>Get familiarised with basic concepts of abacus</span>
                </li>
              </ul>
            </div>

            {/* 10-Class Pack */}
            <div className="bg-gradient-to-br from-[#8B6F47] to-[#6B5335] border-4 border-[#FFD7BA] p-8 rounded-2xl text-white relative shadow-xl">
              <div className="absolute top-0 right-0 bg-[#FFD7BA] text-[#8B6F47] px-4 py-2 text-sm font-bold rounded-bl-2xl">
                BEST VALUE
              </div>
              <h3 className="text-2xl font-semibold mb-2">10-Class Value Pack</h3>
              <div className="text-6xl font-bold mb-4">₹12,500</div>
              <p className="mb-6 opacity-90">Embark on a transformative journey with our Abacus Mastery Package.</p>
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="w-full bg-[#FFD7BA] text-[#8B6F47] py-3 rounded-full font-semibold hover:bg-white transition transform hover:scale-105"
              >
                Get Started
              </button>
              <ul className="mt-6 space-y-2 text-sm">
                {[
                  "Structured Learning Path: Levels-based program",
                  "Consistent Progress: Ensuring steady improvement",
                  "Weekly classes for 3 months",
                  "Exclusive access to books and worksheets",
                  "Priority assistance from instructors"
                ].map((benefit, index) => (
                  <li key={index} className="flex items-start opacity-90">
                    <CheckCircle className="w-5 h-5 mr-2 flex-shrink-0" />
                    <span>{benefit}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-[#FAF3E0] to-[#FFD7BA]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-[#8B6F47] mb-4">What Parents Are Saying</h2>
            <p className="text-xl text-gray-700">Real feedback from happy families</p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { name: 'Hanna M', age: 36, text: "Mrs. Nidhi is an excellent abacus teacher! My child's confidence in math has grown tremendously, and she now loves solving problems. The classes are engaging and well-structured." },
              { name: 'Tara S', age: 28, text: 'The abacus classes by Mrs. Nidhi are fantastic. My daughter not only improved her math skills but also her concentration and problem-solving abilities.' },
              { name: 'Jordan H', age: 34, text: 'Speedy Scholars has been a game-changer for my son. Mrs. Nidhi is patient and makes learning the abacus fun and interactive. His mental calculation skills have improved so much!' },
              { name: 'Joel G', age: 41, text: "Mrs. Nidhi brings out the best in every student. My son's mental arithmetic skills have developed rapidly, and he looks forward to the abacus class every week." }
            ].map((testimonial, idx) => (
              <div key={idx} className="bg-white p-6 rounded-2xl hover:shadow-lg transition border-2 border-[#E8B4A0]">
                <div className="flex mb-4">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-yellow-400 fill-current" />
                  ))}
                </div>
                <p className="text-gray-700 mb-4 italic">"{testimonial.text}"</p>
                <div className="font-semibold text-[#8B6F47]">{testimonial.name}, {testimonial.age}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-[#C9B8A8] to-[#A89F91]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-white mb-4">Get In Touch</h2>
            <p className="text-xl text-white opacity-90">We're here to answer any questions</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="text-center p-6 bg-white bg-opacity-90 rounded-2xl">
              <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center mx-auto mb-4">
                <Phone className="w-7 h-7 text-white" />
              </div>
              <h3 className="font-bold text-[#8B6F47] mb-2">Call Us</h3>
              <p className="text-gray-700">+91 XXX XXX XXXX</p>
            </div>
            <div className="text-center p-6 bg-white bg-opacity-90 rounded-2xl">
              <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center mx-auto mb-4">
                <Mail className="w-7 h-7 text-white" />
              </div>
              <h3 className="font-bold text-[#8B6F47] mb-2">Email Us</h3>
              <p className="text-gray-700">info@speedyscholars.com</p>
            </div>
            <div className="text-center p-6 bg-white bg-opacity-90 rounded-2xl">
              <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center mx-auto mb-4">
                <MapPin className="w-7 h-7 text-white" />
              </div>
              <h3 className="font-bold text-[#8B6F47] mb-2">Location</h3>
              <p className="text-gray-700">Online Classes</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-[#FFF8E7] text-[#8B6F47] py-16 px-4 md:px-8 lg:px-16 border-t-2 border-[#E8B4A0]">
        <div className="max-w-7xl mx-auto">
          <div className="mb-12">
            <h2 className="text-4xl font-bold mb-2">Speedy Scholars</h2>
            <p className="text-xl">Abacus Studio</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div>
              <h3 className="text-lg font-semibold mb-4">Socials</h3>
              <ul className="space-y-2 text-xl font-bold">
                <li><a href="#" className="hover:text-[#E8B4A0] transition">FACEBOOK</a></li>
                <li><a href="#" className="hover:text-[#E8B4A0] transition">YOUTUBE</a></li>
                <li><a href="#" className="hover:text-[#E8B4A0] transition">INSTAGRAM</a></li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4">The Studio</h3>
              <ul className="space-y-2 text-xl font-bold">
                <li><a href="#about" className="hover:text-[#E8B4A0] transition">ABOUT</a></li>
                <li><a href="#pricing" className="hover:text-[#E8B4A0] transition">PRICING</a></li>
                <li><a href="#contact" className="hover:text-[#E8B4A0] transition">CONTACT</a></li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-4">Join</h3>
              <ul className="space-y-2 text-xl font-bold">
                <li><a href="#pricing" className="hover:text-[#E8B4A0] transition">CLASSES</a></li>
                <li><button onClick={() => setIsCalendlyOpen(true)} className="hover:text-[#E8B4A0] transition text-left">BOOK A CLASS</button></li>
              </ul>
            </div>
          </div>

          <div className="border-t border-[#E8B4A0] pt-8 flex flex-col md:flex-row justify-between items-center text-sm">
            <div className="space-x-4 mb-4 md:mb-0">
              <a href="#" className="hover:text-[#E8B4A0] transition">Terms & Conditions</a>
              <a href="#" className="hover:text-[#E8B4A0] transition">Privacy Policy</a>
            </div>
            <div>
              © 2025 by Speedy Scholars.
            </div>
          </div>
        </div>
      </footer>

      {/* Calendly Modal */}
      <CalendlyModal isOpen={isCalendlyOpen} onClose={() => setIsCalendlyOpen(false)} />
    </div>
  );
}