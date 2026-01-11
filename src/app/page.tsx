"use client"

import React, { useState, useEffect, useRef } from 'react';
import { CheckCircle, Phone, Mail, MapPin, Star, Users, Menu, X, Zap, TrendingUp, Globe, Award, GraduationCap, ArrowRight } from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';
import { useCurrency, CurrencySelector } from '@/contexts/CurrencyContext';

// Calendly Modal with iframe embed
function CalendlyModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      setIsLoading(true);
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Modal */}
      <div className="relative w-full max-w-4xl bg-white rounded-3xl shadow-2xl overflow-hidden animate-in fade-in zoom-in duration-300 h-[90vh] flex flex-col">
        {/* Header */}
        <div className="bg-gradient-to-r from-[#8B6F47] to-[#6B5335] px-6 py-4 flex items-center justify-between flex-shrink-0">
          <div>
            <h3 className="text-xl font-bold text-white">Book Your Free Demo Class</h3>
            <p className="text-white/80 text-sm">Choose a time that works best for you</p>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-white/20 rounded-full transition-colors"
          >
            <X className="w-6 h-6 text-white" />
          </button>
        </div>

        {/* Calendly Embed via iframe */}
        <div className="flex-1 relative bg-white">
          {/* Loading State */}
          {isLoading && (
            <div className="absolute inset-0 flex items-center justify-center bg-white z-10">
              <div className="text-center">
                <div className="w-12 h-12 border-4 border-[#8B6F47] border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
                <p className="text-gray-600 font-medium">Loading calendar...</p>
              </div>
            </div>
          )}
          <iframe
            src="https://calendly.com/nidhikhariwal2012/30min?hide_gdpr_banner=1"
            width="100%"
            height="100%"
            frameBorder="0"
            title="Schedule a demo class"
            className="w-full h-full"
            onLoad={() => setIsLoading(false)}
          />
        </div>
      </div>
    </div>
  );
}

// Animated Counter Component
function AnimatedCounter({ end, duration = 2000, suffix = '' }: { end: number; duration?: number; suffix?: string }) {
  const [count, setCount] = useState(0);
  const [hasAnimated, setHasAnimated] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !hasAnimated) {
          setHasAnimated(true);
          let start = 0;
          const increment = end / (duration / 16);
          const timer = setInterval(() => {
            start += increment;
            if (start >= end) {
              setCount(end);
              clearInterval(timer);
            } else {
              setCount(Math.floor(start));
            }
          }, 16);
        }
      },
      { threshold: 0.5 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [end, duration, hasAnimated]);

  return <div ref={ref}>{count}{suffix}</div>;
}

// Feature Card Component
function FeatureCard({ icon: Icon, title, description, image, delay = 0 }: {
  icon?: React.ElementType;
  title: string;
  description: string;
  image?: string;
  delay?: number;
}) {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setTimeout(() => setIsVisible(true), delay);
        }
      },
      { threshold: 0.2 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [delay]);

  return (
    <div
      ref={ref}
      className={`group bg-white rounded-3xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500 transform ${
        isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
      }`}
    >
      {image ? (
        <div className="relative h-48 overflow-hidden">
          <Image
            src={image}
            alt={title}
            fill
            sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
            className="object-cover transition-transform duration-500 group-hover:scale-110"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent" />
        </div>
      ) : Icon && (
        <div className="p-8 pb-0">
          <div className="w-16 h-16 bg-gradient-to-br from-[#F5EDE3] to-[#E8DED0] rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <Icon className="w-8 h-8 text-[#8B6F47]" />
          </div>
        </div>
      )}
      <div className="p-8 pt-6">
        <h3 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-[#8B6F47] transition-colors">{title}</h3>
        <p className="text-gray-600 leading-relaxed">{description}</p>
      </div>
    </div>
  );
}

// Testimonial Card
function TestimonialCard({ name, text, rating = 5, location, delay = 0 }: {
  name: string;
  text: string;
  rating?: number;
  location?: string;
  delay?: number;
}) {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setTimeout(() => setIsVisible(true), delay);
        }
      },
      { threshold: 0.2 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [delay]);

  return (
    <div
      ref={ref}
      className={`bg-white p-8 rounded-3xl shadow-lg hover:shadow-xl transition-all duration-500 border border-gray-100 ${
        isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-8'
      }`}
    >
      <div className="flex gap-1 mb-4">
        {[...Array(rating)].map((_, i) => (
          <Star key={i} className="w-5 h-5 text-[#C9A86C] fill-current" />
        ))}
      </div>
      <p className="text-gray-700 mb-6 leading-relaxed italic">&ldquo;{text}&rdquo;</p>
      <div className="flex items-center gap-3">
        <div className="w-12 h-12 rounded-full bg-gradient-to-br from-[#E8DED0] to-[#D4C4B0] flex items-center justify-center">
          <span className="text-[#6B5335] font-bold text-lg">{name.charAt(0)}</span>
        </div>
        <div>
          <div className="font-semibold text-gray-900">{name}</div>
          {location && <div className="text-sm text-gray-500">{location}</div>}
        </div>
      </div>
    </div>
  );
}

// Pricing Card
function PricingCard({
  title,
  price,
  period,
  description,
  features,
  isPopular,
  onBook,
  formatPrice
}: {
  title: string;
  price: number | string;
  period?: string;
  description: string;
  features: string[];
  isPopular?: boolean;
  onBook: () => void;
  formatPrice: (price: number) => string;
}) {
  return (
    <div className={`relative rounded-3xl p-8 transition-all duration-300 hover:scale-105 ${
      isPopular
        ? 'bg-gradient-to-br from-[#8B6F47] to-[#5A4830] text-white shadow-2xl scale-105 lg:scale-110'
        : 'bg-white shadow-xl border border-gray-100'
    }`}>
      {isPopular && (
        <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-[#C9A86C] to-[#D4B896] text-[#5A4830] px-6 py-2 rounded-full text-sm font-bold shadow-lg">
          MOST POPULAR
        </div>
      )}

      <h3 className={`text-2xl font-bold mb-2 ${isPopular ? 'text-white' : 'text-gray-900'}`}>{title}</h3>

      <div className="mb-4">
        <span className={`text-5xl font-bold ${isPopular ? 'text-white' : 'text-[#8B6F47]'}`}>
          {typeof price === 'number' ? formatPrice(price) : price}
        </span>
        {period && <span className={`text-sm ${isPopular ? 'text-white/70' : 'text-gray-500'}`}> {period}</span>}
      </div>

      <p className={`mb-6 ${isPopular ? 'text-white/80' : 'text-gray-600'}`}>{description}</p>

      <button
        onClick={onBook}
        className={`w-full py-4 rounded-2xl font-semibold transition-all duration-300 mb-6 ${
          isPopular
            ? 'bg-white text-[#6B5335] hover:bg-stone-50'
            : 'bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white hover:from-[#7A6040] hover:to-[#5A4830]'
        }`}
      >
        Get Started
      </button>

      <ul className="space-y-3">
        {features.map((feature, idx) => (
          <li key={idx} className="flex items-start gap-3">
            <CheckCircle className={`w-5 h-5 flex-shrink-0 mt-0.5 ${isPopular ? 'text-[#C9A86C]' : 'text-[#8B6F47]'}`} />
            <span className={isPopular ? 'text-white/90' : 'text-gray-600'}>{feature}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default function SpeedyScholarsLanding() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isCalendlyOpen, setIsCalendlyOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  const { formatPrice } = useCurrency();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { href: "#benefits", label: "Why Abacus" },
    { href: "#instructor", label: "Instructor" },
    { href: "#pricing", label: "Pricing" },
    { href: "#testimonials", label: "Reviews" },
  ];

  const features = [
    {
      image: "/images/kid2.jpg",
      title: "Lightning-Fast Mental Math",
      description: "Students learn to perform complex calculations mentally in seconds. Research shows abacus learners calculate 3-4x faster."
    },
    {
      image: "/images/brain2.jpeg",
      title: "Enhanced Brain Development",
      description: "Activates both brain hemispheres, improving cognitive function, memory, and concentration."
    },
    {
      image: "/images/study.jpeg",
      title: "Improved Focus & Concentration",
      description: "Regular practice significantly enhances attention span, benefiting all areas of academics."
    },
    {
      image: "/images/imagination.jpeg",
      title: "Visualization Skills",
      description: "Develop strong mental imagery abilities essential for problem-solving across subjects."
    },
    {
      image: "/images/goal.jpeg",
      title: "Confidence Booster",
      description: "Mastering mental math builds self-confidence and eliminates math anxiety."
    },
    {
      image: "/images/class.jpeg",
      title: "Academic Excellence",
      description: "Abacus students show improved performance across all subjects with better analytical thinking."
    }
  ];

  const testimonials = [
    {
      name: "Hanna M.",
      text: "Mrs. Nidhi is an excellent abacus teacher! My child's confidence in math has grown tremendously, and she now loves solving problems.",
      location: "Parent, USA"
    },
    {
      name: "Tara S.",
      text: "The abacus classes are fantastic. My daughter not only improved her math skills but also her concentration and problem-solving abilities.",
      location: "Parent, UK"
    },
    {
      name: "Jordan H.",
      text: "Speedy Scholars has been a game-changer for my son. Mrs. Nidhi is patient and makes learning fun. His mental calculation skills improved so much!",
      location: "Parent, Australia"
    },
    {
      name: "Joel G.",
      text: "Mrs. Nidhi brings out the best in every student. My son's mental arithmetic skills have developed rapidly, and he looks forward to class every week.",
      location: "Parent, India"
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-stone-50 to-white">
      {/* Premium Navigation */}
      <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
        isScrolled
          ? 'bg-white/95 backdrop-blur-lg shadow-lg py-3'
          : 'bg-transparent py-5'
      }`}>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <Link href="/" className="flex items-center gap-3">
              <Image
                src="/images/logo.png"
                alt="Speedy Scholars"
                width={56}
                height={56}
                className={`transition-all duration-300 ${isScrolled ? 'w-12 h-12' : 'w-14 h-14'}`}
              />
              <span className={`font-bold transition-all duration-300 ${
                isScrolled ? 'text-gray-900 text-lg' : 'text-white text-xl'
              }`}>
                Speedy Scholars
              </span>
            </Link>

            <div className="hidden md:flex items-center gap-8">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className={`font-medium transition-colors ${
                    isScrolled ? 'text-gray-700 hover:text-[#8B6F47]' : 'text-white/90 hover:text-white'
                  }`}
                >
                  {link.label}
                </a>
              ))}
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className={`px-6 py-2.5 rounded-full font-semibold transition-all duration-300 ${
                  isScrolled
                    ? 'bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white hover:shadow-lg hover:scale-105'
                    : 'bg-white text-[#6B5335] hover:bg-stone-50'
                }`}
              >
                Book Free Demo
              </button>
            </div>

            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className={`md:hidden p-2 rounded-lg ${isScrolled ? 'text-gray-700' : 'text-white'}`}
            >
              {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>

          {/* Mobile Menu */}
          {isMobileMenuOpen && (
            <div className="md:hidden mt-4 pb-4 space-y-3 bg-white rounded-2xl p-4 shadow-xl">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="block text-gray-700 hover:text-[#8B6F47] font-medium py-2"
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
                className="w-full bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white py-3 rounded-xl font-semibold"
              >
                Book Free Demo
              </button>
            </div>
          )}
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center overflow-hidden">
        {/* Video Background */}
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
        >
          <source src="/images/abacusVideo.mp4" type="video/mp4" />
        </video>

        {/* Subtle Gradient Overlay - lets video show through */}
        <div className="absolute inset-0 bg-gradient-to-br from-stone-900/40 via-stone-800/30 to-black/50" />

        {/* Content */}
        <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32">
          <div className="max-w-3xl">
            {/* Badge */}
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-5 py-2 mb-8">
              <span className="flex h-2 w-2 relative">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#C9A86C] opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#C9A86C]"></span>
              </span>
              <span className="text-white font-medium">Limited Time: First Demo Class FREE</span>
            </div>

            {/* Headline */}
            <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-tight">
              Unlock Your Child&apos;s{' '}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#D4B896] to-[#C9A86C]">
                Mathematical Genius
              </span>
            </h1>

            <p className="text-xl md:text-2xl text-white/90 mb-10 leading-relaxed max-w-2xl">
              Transform mental arithmetic into an exciting adventure. Build confidence, improve focus, and develop lifelong skills with expert abacus training.
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 mb-12">
              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="group inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#8B6F47] to-[#6B5335] text-white px-8 py-4 rounded-full font-semibold text-lg hover:from-[#7A6040] hover:to-[#5A4830] transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-105"
              >
                Claim Your Free Demo
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </button>
              <a
                href="#benefits"
                className="inline-flex items-center justify-center gap-2 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-white/20 transition-all duration-300"
              >
                Learn More
              </a>
            </div>

            {/* Trust Indicators */}
            <div className="flex flex-wrap gap-8 items-center">
              <div className="flex items-center gap-2">
                <div className="flex -space-x-2">
                  {[1,2,3,4].map((i) => (
                    <div key={i} className="w-10 h-10 rounded-full bg-gradient-to-br from-[#D4B896] to-[#C9A86C] border-2 border-white flex items-center justify-center">
                      <span className="text-xs font-bold text-[#5A4830]">{String.fromCharCode(64 + i)}</span>
                    </div>
                  ))}
                </div>
                <div className="text-white">
                  <div className="font-semibold">2,000+ Students</div>
                  <div className="text-sm text-white/70">Worldwide</div>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <div className="flex">
                  {[...Array(5)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-[#C9A86C] fill-current" />
                  ))}
                </div>
                <span className="text-white font-medium">4.9/5 Rating</span>
              </div>
            </div>
          </div>
        </div>

        {/* Scroll Indicator */}
        <div className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 animate-bounce">
          <span className="text-white/70 text-sm">Scroll to explore</span>
          <div className="w-6 h-10 rounded-full border-2 border-white/30 flex justify-center pt-2">
            <div className="w-1.5 h-3 bg-white/70 rounded-full animate-pulse" />
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {[
              { value: 20, suffix: '+', label: 'Years Experience' },
              { value: 2000, suffix: '+', label: 'Students Taught' },
              { value: 50, suffix: '+', label: 'Competition Winners' },
              { value: 15, suffix: '+', label: 'Awards Won' }
            ].map((stat, idx) => (
              <div key={idx} className="text-center">
                <div className="text-4xl md:text-5xl font-bold text-[#8B6F47] mb-2">
                  <AnimatedCounter end={stat.value} suffix={stat.suffix} />
                </div>
                <div className="text-gray-600">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Abacus Section */}
      <section id="benefits" className="py-24 bg-gradient-to-b from-white to-stone-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <span className="inline-block bg-[#F5EDE3] text-[#8B6F47] px-4 py-1.5 rounded-full text-sm font-semibold mb-4">
              WHY ABACUS?
            </span>
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              The Ancient Tool for Modern Minds
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Discover how abacus training transforms children into confident mathematical thinkers
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, idx) => (
              <FeatureCard key={idx} {...feature} delay={idx * 100} />
            ))}
          </div>
        </div>
      </section>

      {/* Meet Instructor Section */}
      <section id="instructor" className="py-24 bg-gradient-to-br from-[#5A4830] to-[#3D3020] text-white overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            {/* Image Side */}
            <div className="relative">
              <div className="relative z-10 rounded-3xl overflow-hidden shadow-2xl">
                <Image
                  src="/images/founder.jpeg"
                  alt="Nidhi Khariwal - Founder of Speedy Scholars"
                  width={600}
                  height={700}
                  className="w-full h-auto object-cover"
                />
              </div>

              {/* Decorative Elements */}
              <div className="absolute -top-8 -left-8 w-24 h-24 bg-[#C9A86C]/20 rounded-full blur-2xl" />
              <div className="absolute -bottom-8 -right-8 w-32 h-32 bg-[#D4B896]/20 rounded-full blur-2xl" />

              {/* Floating Badge */}
              <div className="absolute bottom-4 right-4 md:bottom-6 md:right-6 z-20 bg-white text-[#6B5335] px-6 py-4 rounded-2xl shadow-xl">
                <div className="text-3xl font-bold">20+</div>
                <div className="text-sm font-medium">Years of Excellence</div>
              </div>
            </div>

            {/* Content Side */}
            <div>
              <span className="inline-block bg-white/10 text-[#D4B896] px-4 py-1.5 rounded-full text-sm font-semibold mb-6">
                MEET YOUR INSTRUCTOR
              </span>

              <h2 className="text-4xl md:text-5xl font-bold mb-4">Nidhi Khariwal</h2>
              <p className="text-[#D4B896] text-xl mb-6">Founder & Lead Instructor</p>

              <p className="text-white/80 text-lg leading-relaxed mb-8">
                With over <strong className="text-white">20 years of dedicated experience</strong> in teaching abacus, mental arithmetic, and English, Mrs. Nidhi has transformed the lives of more than <strong className="text-white">2,000+ students</strong> worldwide. Fluent in both <strong className="text-white">English and Hindi</strong>, she provides personalized instruction to students across the globe, making her one of the most sought-after abacus educators for international families.
              </p>

              <div className="grid grid-cols-2 gap-4 mb-8">
                {[
                  { icon: Award, label: 'Award-Winning Educator' },
                  { icon: GraduationCap, label: 'Certified Trainer' },
                  { icon: Users, label: 'Competition Coach' },
                  { icon: Globe, label: 'English & Hindi Classes' }
                ].map((item, idx) => (
                  <div key={idx} className="flex items-center gap-3 bg-white/10 rounded-xl p-3">
                    <item.icon className="w-5 h-5 text-[#C9A86C]" />
                    <span className="text-sm font-medium">{item.label}</span>
                  </div>
                ))}
              </div>

              <button
                onClick={() => setIsCalendlyOpen(true)}
                className="inline-flex items-center gap-2 bg-white text-[#6B5335] px-8 py-4 rounded-full font-semibold hover:bg-stone-50 transition-all duration-300 shadow-lg hover:shadow-xl"
              >
                Book a Session with Mrs. Nidhi
                <ArrowRight className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section id="pricing" className="py-24 bg-gradient-to-b from-stone-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <span className="inline-block bg-[#F5EDE3] text-[#8B6F47] px-4 py-1.5 rounded-full text-sm font-semibold mb-4">
              PRICING
            </span>
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              Simple, Transparent Pricing
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto mb-6">
              Choose the plan that works best for your family
            </p>

            {/* Currency Selector */}
            <div className="inline-flex items-center gap-3 bg-white px-4 py-2 rounded-full shadow-md border border-gray-100">
              <Globe className="w-5 h-5 text-gray-500" />
              <span className="text-gray-600 text-sm">Showing prices in:</span>
              <CurrencySelector className="text-sm" />
            </div>
          </div>

          <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            <PricingCard
              title="Demo Class"
              price="FREE"
              description="Perfect for trying out our teaching style"
              features={[
                "45-minute session",
                "Meet your instructor",
                "Assess current skill level",
                "Get personalized recommendations",
                "No commitment required"
              ]}
              onBook={() => setIsCalendlyOpen(true)}
              formatPrice={formatPrice}
            />

            <PricingCard
              title="10-Class Pack"
              price={12500}
              period="/ 10 classes"
              description="Our most popular choice for serious learners"
              features={[
                "Structured learning path",
                "Weekly progress tracking",
                "Books & worksheets included",
                "Priority scheduling",
                "Parent progress reports",
                "Competition preparation"
              ]}
              isPopular
              onBook={() => setIsCalendlyOpen(true)}
              formatPrice={formatPrice}
            />

            <PricingCard
              title="Pay-As-You-Go"
              price={1600}
              period="/ class"
              description="Flexible option for busy families"
              features={[
                "45-minute sessions",
                "Book anytime",
                "No long-term commitment",
                "Flexible scheduling",
                "Session recordings available"
              ]}
              onBook={() => setIsCalendlyOpen(true)}
              formatPrice={formatPrice}
            />
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <span className="inline-block bg-[#F5EDE3] text-[#8B6F47] px-4 py-1.5 rounded-full text-sm font-semibold mb-4">
              TESTIMONIALS
            </span>
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
              What Parents Are Saying
            </h2>
            <p className="text-xl text-gray-600">Real feedback from happy families around the world</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {testimonials.map((testimonial, idx) => (
              <TestimonialCard key={idx} {...testimonial} delay={idx * 100} />
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 bg-gradient-to-br from-[#8B6F47] to-[#5A4830]">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Ready to Transform Your Child&apos;s Math Skills?
          </h2>
          <p className="text-xl text-white/90 mb-10 max-w-2xl mx-auto">
            Join thousands of parents who have seen remarkable improvements in their children&apos;s confidence and abilities.
          </p>
          <button
            onClick={() => setIsCalendlyOpen(true)}
            className="inline-flex items-center gap-2 bg-white text-[#6B5335] px-10 py-5 rounded-full font-bold text-lg hover:bg-stone-50 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-105"
          >
            Book Your Free Demo Class Today
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-24 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Get In Touch</h2>
            <p className="text-xl text-gray-600">We&apos;re here to answer any questions</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            {[
              { icon: Phone, title: 'Call Us', info: '+91 9352646671', sub: 'Mon-Sat, 9AM-7PM IST' },
              { icon: Mail, title: 'Email Us', info: 'nidhikhariwal2012@gmail.com', sub: 'Reply within 24 hours' },
              { icon: MapPin, title: 'Location', info: 'Online Classes', sub: 'Learn from anywhere' }
            ].map((item, idx) => (
              <div key={idx} className="bg-white rounded-2xl p-8 text-center shadow-lg hover:shadow-xl transition-shadow">
                <div className="w-14 h-14 bg-gradient-to-br from-[#F5EDE3] to-[#E8DED0] rounded-2xl flex items-center justify-center mx-auto mb-4">
                  <item.icon className="w-7 h-7 text-[#8B6F47]" />
                </div>
                <h3 className="font-bold text-gray-900 mb-2">{item.title}</h3>
                <p className="text-gray-700 font-medium">{item.info}</p>
                <p className="text-sm text-gray-500">{item.sub}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-12 mb-12">
            <div className="md:col-span-2">
              <div className="flex items-center gap-3 mb-4">
                <Image src="/images/logo.png" alt="Speedy Scholars" width={48} height={48} />
                <span className="text-xl font-bold">Speedy Scholars</span>
              </div>
              <p className="text-gray-400 mb-6 max-w-md">
                Empowering children with mathematical confidence through expert abacus training. Join thousands of happy families worldwide.
              </p>
              <div className="flex gap-4">
                {['facebook', 'youtube', 'instagram'].map((social) => (
                  <a key={social} href="#" className="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center hover:bg-[#8B6F47] transition-colors">
                    <span className="sr-only">{social}</span>
                    <div className="w-5 h-5 bg-white/70 rounded" />
                  </a>
                ))}
              </div>
            </div>

            <div>
              <h4 className="font-semibold mb-4">Quick Links</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#benefits" className="hover:text-white transition-colors">Why Abacus</a></li>
                <li><a href="#instructor" className="hover:text-white transition-colors">Our Instructor</a></li>
                <li><a href="#pricing" className="hover:text-white transition-colors">Pricing</a></li>
                <li><a href="#testimonials" className="hover:text-white transition-colors">Reviews</a></li>
                <li><Link href="/contact" className="hover:text-white transition-colors">Contact</Link></li>
              </ul>
            </div>

            <div>
              <h4 className="font-semibold mb-4">Contact</h4>
              <ul className="space-y-2 text-gray-400">
                <li>+91 9352646671</li>
                <li>nidhikhariwal2012@gmail.com</li>
                <li>Online Classes Worldwide</li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
            <p>&copy; 2025 Speedy Scholars. All rights reserved.</p>
            <div className="flex gap-6 mt-4 md:mt-0">
              <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
              <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
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
        <svg className="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
          <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
        <span className="absolute right-full mr-3 top-1/2 -translate-y-1/2 bg-white text-gray-800 px-4 py-2 rounded-xl shadow-lg text-sm font-medium whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          Chat with us!
        </span>
      </a>
    </div>
  );
}
