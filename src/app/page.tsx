"use client"

import React, { useState, useEffect, useCallback } from 'react';
import { CheckCircle, Phone, Mail, MapPin, Star, Users, BookOpen, Clock, Menu, X, Target, Zap, TrendingUp, Sparkles, ChevronLeft, ChevronRight, Globe } from 'lucide-react';
import Image from 'next/image';
import { useCurrency, CurrencySelector } from '@/contexts/CurrencyContext';

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
          <h3 className="text-3xl font-bold text-[#8B6F47] mb-4 text-center">Book Your Free 45-Minute Demo Class</h3>
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

// Carousel Component
function WhyScholarsCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);
  
  const benefits = [
    {
      image: "/images/class.jpeg",
      title: "Expert Instruction",
      description: "Learn from Mrs. Nidhi, a certified and passionate abacus educator with years of experience in transforming young minds."
    },
    {
      icon: Users,
      title: "Small Class Sizes",
      description: "We maintain small class sizes to ensure every child receives personalized attention and guidance tailored to their learning pace."
    },
    {
      image: "/images/student.jpeg",
      title: "Flexible Online Classes",
      description: "Learn from the comfort of home with our interactive online sessions. Schedule classes at times that work for your family."
    },
    {
      icon: BookOpen,
      title: "Level-Based Learning",
      description: "Our structured, level-based curriculum ensures steady progress from foundational concepts to advanced mental calculation techniques."
    },
    {
      icon: Target,
      title: "Regular Progress Updates",
      description: "Parents receive regular updates on their child's progress, with detailed feedback and milestone achievements."
    },
    {
      icon: Sparkles,
      title: "Fun & Engaging",
      description: "We make learning enjoyable with interactive activities, games, and challenges that keep children motivated and excited."
    }
  ];

  const cardsToShow = 3;
  const maxIndex = benefits.length - cardsToShow;

  const nextSlide = useCallback(() => {
    setCurrentIndex((prev) => (prev >= maxIndex ? 0 : prev + 1));
  }, [maxIndex]);

  const prevSlide = useCallback(() => {
    setCurrentIndex((prev) => (prev <= 0 ? maxIndex : prev - 1));
  }, [maxIndex]);

  return (
    <div className="relative">
      <div className="overflow-hidden">
        <div 
          className="flex transition-transform duration-500 ease-out"
          style={{ transform: `translateX(-${currentIndex * (100 / cardsToShow)}%)` }}
        >
          {benefits.map((benefit, idx) => (
            <div key={idx} className="w-full md:w-1/3 flex-shrink-0 px-4">
              <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition h-full">
                {benefit.image ? (
                  <div className="mb-6 rounded-2xl overflow-hidden">
                    <Image 
                      src={benefit.image}
                      alt={benefit.title}
                      width={300} 
                      height={200}
                      className="w-full h-48 object-cover"
                    />
                  </div>
                ) : benefit.icon && (
                  <div className="w-16 h-16 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-2xl flex items-center justify-center mb-6">
                    <benefit.icon className="w-8 h-8 text-white" />
                  </div>
                )}
                <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">{benefit.title}</h3>
                <p className="text-gray-700 leading-relaxed">{benefit.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Navigation Buttons */}
      <button
        onClick={prevSlide}
        className="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-4 w-12 h-12 bg-white rounded-full shadow-xl flex items-center justify-center hover:bg-[#FFD7BA] transition z-10"
        aria-label="Previous slide"
      >
        <ChevronLeft className="w-6 h-6 text-[#8B6F47]" />
      </button>
      <button
        onClick={nextSlide}
        className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-4 w-12 h-12 bg-white rounded-full shadow-xl flex items-center justify-center hover:bg-[#FFD7BA] transition z-10"
        aria-label="Next slide"
      >
        <ChevronRight className="w-6 h-6 text-[#8B6F47]" />
      </button>

      {/* Dots Indicator */}
      <div className="flex justify-center gap-2 mt-8">
        {Array.from({ length: maxIndex + 1 }).map((_, idx) => (
          <button
            key={idx}
            onClick={() => setCurrentIndex(idx)}
            className={`w-3 h-3 rounded-full transition ${
              idx === currentIndex ? 'bg-[#8B6F47] w-8' : 'bg-[#E8B4A0]'
            }`}
            aria-label={`Go to slide ${idx + 1}`}
          />
        ))}
      </div>
    </div>
  );
}

// Pricing Section Component with Currency Support
function PricingSection({ onBookDemo }: { onBookDemo: () => void }) {
  const { formatPrice } = useCurrency();

  return (
    <section id="pricing" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7]">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-[#8B6F47] mb-4">Simple, Transparent Pricing</h2>
          <p className="text-xl text-gray-700 mb-6">Choose the plan that works best for your family</p>

          {/* Currency Selector */}
          <div className="flex items-center justify-center gap-3">
            <Globe className="w-5 h-5 text-[#8B6F47]" />
            <span className="text-gray-600 text-sm">Showing prices in:</span>
            <CurrencySelector className="text-sm" />
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {/* Demo Class */}
          <div className="bg-gradient-to-br from-[#C9B8A8] to-[#A89F91] border-2 border-[#8B6F47] p-8 rounded-2xl text-white shadow-xl">
            <h3 className="text-2xl font-semibold mb-2">Demo Class</h3>
            <div className="text-5xl font-bold mb-4">FREE</div>
            <p className="mb-6 opacity-90">First 45 Mins Abacus Class is on us.</p>
            <button
              onClick={onBookDemo}
              className="w-full bg-white text-[#8B6F47] py-3 rounded-full font-semibold hover:bg-[#FFD7BA] transition transform hover:scale-105"
            >
              Book Now
            </button>
          </div>

          {/* Pay-As-You-Go */}
          <div className="bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] border-2 border-[#8B6F47] p-8 rounded-2xl text-white shadow-xl">
            <h3 className="text-2xl font-semibold mb-2">Pay-As-You-Go</h3>
            <div className="text-5xl font-bold mb-2">{formatPrice(1600)}</div>
            <p className="text-sm opacity-75 mb-4">per class</p>
            <p className="mb-6 opacity-90">Experience flexible learning with our Single Session Pass.</p>
            <button
              onClick={onBookDemo}
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
            <div className="text-5xl font-bold mb-2">{formatPrice(12500)}</div>
            <p className="text-sm opacity-75 mb-4">{formatPrice(1250)}/class • Save 22%</p>
            <p className="mb-6 opacity-90">Embark on a transformative journey with our Abacus Mastery Package.</p>
            <button
              onClick={onBookDemo}
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
  );
}

export default function SpeedyScholarsLanding() {
  const [, setIsVisible] = useState(false);
  const [, setIsVideoLoaded] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isCalendlyOpen, setIsCalendlyOpen] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const navLinks = [
    { href: "#benefits", label: "Why Abacus" },
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
            <a href="#" className="flex items-center space-x-3">
              <Image src="/images/logo.png" alt="Speedy Scholars Logo" width={80} height={80} className="h-20 w-20" />
              <span className="text-xl font-bold text-white hidden sm:block">Speedy Scholars</span>
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
            🎁 First 45-Minute Demo Class FREE!
          </div>
          
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold mb-6 drop-shadow-lg">
            Unlock Your Child&apos;s
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
              Claim Your Free Demo Class
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
        <div className="absolute bottom-0 left-0 w-full h-16 flex justify-around items-end overflow-hidden z-20">
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

      {/* Why Abacus - Benefits Section */}
      <section id="benefits" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold text-[#8B6F47] mb-4">Why Abacus?</h2>
            <p className="text-xl text-gray-700">The Ancient Tool for Modern Minds</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Lightning-Fast Mental Math */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="w-16 h-16 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-2xl flex items-center justify-center mb-6">
                <Zap className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Lightning-Fast Mental Math</h3>
              <p className="text-gray-700 leading-relaxed">
                Students learn to perform complex calculations mentally in seconds. Research shows abacus learners can calculate 3-4 times faster than traditional methods.
              </p>
            </div>

            {/* Enhanced Brain Development */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="mb-6 rounded-2xl overflow-hidden">
                <Image 
                  src="/images/brain2.jpeg" 
                  alt="Brain Development" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Enhanced Brain Development</h3>
              <p className="text-gray-700 leading-relaxed">
                Activates both left and right hemispheres of the brain, improving overall cognitive function, memory, and concentration.
              </p>
            </div>

            {/* Improved Concentration */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="mb-6 rounded-2xl overflow-hidden">
                <Image 
                  src="/images/study.jpeg" 
                  alt="Focused Learning" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Improved Concentration</h3>
              <p className="text-gray-700 leading-relaxed">
                Regular abacus practice significantly enhances focus and attention span, benefiting all areas of academic performance.
              </p>
            </div>

            {/* Visualization Skills */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="mb-6 rounded-2xl overflow-hidden">
                <Image 
                  src="/images/imagination.jpeg" 
                  alt="Creative Thinking" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Visualization Skills</h3>
              <p className="text-gray-700 leading-relaxed">
                Children develop strong mental imagery and visualization abilities, essential for problem-solving in all subjects.
              </p>
            </div>

            {/* Confidence Booster */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="mb-6 rounded-2xl overflow-hidden">
                <Image 
                  src="/images/goal.jpeg" 
                  alt="Achievement" 
                  width={300} 
                  height={200}
                  className="w-full h-48 object-cover"
                />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Confidence Booster</h3>
              <p className="text-gray-700 leading-relaxed">
                Mastering mental math builds self-confidence and reduces math anxiety, creating a positive attitude towards learning.
              </p>
            </div>

            {/* Academic Excellence */}
            <div className="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition transform hover:-translate-y-2">
              <div className="w-16 h-16 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-2xl flex items-center justify-center mb-6">
                <TrendingUp className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold text-[#8B6F47] mb-4">Academic Excellence</h3>
              <p className="text-gray-700 leading-relaxed">
                Students who learn abacus show improved performance across all subjects, with better memory retention and analytical thinking.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Why Speedy Scholars Section - Carousel */}
      <section className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-[#FAF3E0] to-[#FFD7BA]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <div className="inline-block bg-white px-6 py-3 rounded-full shadow-lg mb-6">
              <div className="flex items-center space-x-2">
                <Star className="w-5 h-5 text-yellow-500 fill-current" />
                <span className="font-bold text-[#8B6F47]">4.9/5</span>
                <span className="text-gray-600 text-sm">from parents</span>
              </div>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold text-[#8B6F47] mb-4">Why Choose Speedy Scholars?</h2>
            <p className="text-xl text-gray-700">Excellence in Every Aspect of Learning</p>
          </div>
          
          <WhyScholarsCarousel />
        </div>
      </section>

      {/* Begin Your Learning Journey - CTA Section */}
      <section className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7]">
        <div className="max-w-7xl mx-auto">
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
              <h2 className="text-4xl md:text-5xl font-bold text-[#8B6F47] mb-6">
                Begin Your Learning Journey
              </h2>
              <p className="text-xl text-gray-700 leading-relaxed mb-6">
                Every child learns at their own pace. Our personalized approach ensures that each student receives the attention and guidance they need to excel.
              </p>
              <div className="bg-gradient-to-r from-[#FFD7BA] to-[#E8B4A0] p-6 rounded-2xl mb-6">
                <p className="text-[#8B6F47] font-bold text-lg mb-2">🎁 Special Offer</p>
                <p className="text-[#8B6F47] text-2xl font-bold">Your First 45-Minute Demo Class is FREE!</p>
              </div>
              <p className="text-lg text-gray-700 leading-relaxed mb-8">
                Experience our teaching methodology firsthand. See how your child responds to abacus learning with zero commitment. Book your free demo class today!
              </p>
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white px-10 py-5 rounded-full font-bold text-lg hover:shadow-2xl transition transform hover:scale-105"
              >
                Book Your FREE 45-Minute Demo Class
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Meet Your Instructor Section */}
      <section className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-[#FAF3E0] to-[#FFD7BA]">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl md:text-5xl font-bold text-[#8B6F47] mb-4">Meet Your Instructor</h2>
            <p className="text-xl text-gray-700">Learn from an expert with decades of experience</p>
          </div>

          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="relative">
              <div className="rounded-3xl overflow-hidden shadow-2xl border-4 border-white">
                <Image
                  src="/images/founder.jpeg"
                  alt="Nidhi Khariwal - Founder of Speedy Scholars"
                  width={500}
                  height={600}
                  className="w-full h-auto object-cover"
                />
              </div>
              {/* Decorative badge */}
              <div className="absolute -bottom-4 -right-4 bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white px-6 py-3 rounded-2xl shadow-xl">
                <p className="font-bold text-lg">20+ Years</p>
                <p className="text-sm opacity-90">of Excellence</p>
              </div>
            </div>

            <div>
              <h3 className="text-3xl font-bold text-[#8B6F47] mb-2">Nidhi Khariwal</h3>
              <p className="text-[#E8B4A0] font-semibold text-lg mb-6">Founder & Lead Instructor</p>

              <p className="text-gray-700 text-lg leading-relaxed mb-6">
                With over <strong>20 years of dedicated experience</strong> in teaching abacus and mental arithmetic, Mrs. Nidhi has transformed the lives of more than <strong>2,000+ students</strong> worldwide. Her passion for making math enjoyable and her personalized teaching approach have made her one of the most sought-after abacus educators.
              </p>

              <div className="grid grid-cols-2 gap-4 mb-8">
                <div className="bg-white p-4 rounded-2xl shadow-lg text-center">
                  <div className="text-3xl font-bold text-[#8B6F47]">20+</div>
                  <div className="text-gray-600 text-sm">Years Teaching</div>
                </div>
                <div className="bg-white p-4 rounded-2xl shadow-lg text-center">
                  <div className="text-3xl font-bold text-[#8B6F47]">2000+</div>
                  <div className="text-gray-600 text-sm">Students Trained</div>
                </div>
                <div className="bg-white p-4 rounded-2xl shadow-lg text-center">
                  <div className="text-3xl font-bold text-[#8B6F47]">50+</div>
                  <div className="text-gray-600 text-sm">Competition Winners</div>
                </div>
                <div className="bg-white p-4 rounded-2xl shadow-lg text-center">
                  <div className="text-3xl font-bold text-[#8B6F47]">15+</div>
                  <div className="text-gray-600 text-sm">Awards Received</div>
                </div>
              </div>

              <div className="flex flex-wrap gap-3">
                <span className="bg-[#8B6F47] text-white px-4 py-2 rounded-full text-sm font-medium">Award-Winning Educator</span>
                <span className="bg-[#8B6F47] text-white px-4 py-2 rounded-full text-sm font-medium">Certified Trainer</span>
                <span className="bg-[#8B6F47] text-white px-4 py-2 rounded-full text-sm font-medium">Competition Coach</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <PricingSection onBookDemo={() => setIsCalendlyOpen(true)} />

      {/* Testimonials Section */}
      <section id="testimonials" className="py-20 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#FFF8E7]">
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
                <p className="text-gray-700 mb-4 italic">&ldquo;{testimonial.text}&rdquo;</p>
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
            <p className="text-xl text-white opacity-90">We&apos;re here to answer any questions</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="text-center p-6 bg-white bg-opacity-90 rounded-2xl">
              <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center mx-auto mb-4">
                <Phone className="w-7 h-7 text-white" />
              </div>
              <h3 className="font-bold text-[#8B6F47] mb-2">Call Us</h3>
              <p className="text-gray-700">+91 9352646671</p>
            </div>
            <div className="text-center p-6 bg-white bg-opacity-90 rounded-2xl">
              <div className="w-14 h-14 bg-gradient-to-br from-[#E8B4A0] to-[#D4A89C] rounded-full flex items-center justify-center mx-auto mb-4">
                <Mail className="w-7 h-7 text-white" />
              </div>
              <h3 className="font-bold text-[#8B6F47] mb-2">Email Us</h3>
              <p className="text-gray-700">nidhikhariwal2012@gmail.com</p>
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
                <li><a href="#benefits" className="hover:text-[#E8B4A0] transition">WHY ABACUS</a></li>
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

      {/* WhatsApp Floating Button */}
      <a
        href="https://wa.me/919352646671?text=Hi%2C%20I'm%20interested%20in%20abacus%20classes%20for%20my%20child."
        target="_blank"
        rel="noopener noreferrer"
        className="fixed bottom-6 right-6 z-50 bg-[#25D366] hover:bg-[#128C7E] text-white p-4 rounded-full shadow-2xl transition-all duration-300 hover:scale-110 group"
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
        <span className="absolute right-full mr-3 top-1/2 -translate-y-1/2 bg-white text-gray-800 px-3 py-2 rounded-lg shadow-lg text-sm font-medium whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          Chat with us!
        </span>
      </a>
    </div>
  );
}