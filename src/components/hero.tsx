"use client"

import { Button } from "@/components/ui/button"
import Link from "next/link"
import { useState, useEffect } from "react"
import { motion } from "framer-motion"

export default function HeroSection() {
  const [isVideoLoaded, setIsVideoLoaded] = useState(false)
  const whatsappLink = "https://wa.me/1234567890" // Replace with your actual WhatsApp number

  useEffect(() => {
    const timer = setTimeout(() => setIsVideoLoaded(true), 1000)
    return () => clearTimeout(timer)
  }, [])

  const fadeInUp = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 }
  }

  return (
    <section className="relative h-screen w-full overflow-hidden">
      {/* Background Video */}
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover"
        onLoadedData={() => setIsVideoLoaded(true)}
      >
        <source src="/images/abacusVideo.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      {/* Overlay */}
      <motion.div 
        className="absolute top-0 left-0 w-full h-full bg-black"
        initial={{ opacity: 0 }}
        animate={{ opacity: 0.5 }}
        transition={{ duration: 1.5 }}
      />

      {/* Content */}
      <div className="relative z-10 flex flex-col items-center justify-center h-full text-white px-4 text-center">
        <motion.h1 
          className="text-4xl md:text-6xl lg:text-7xl font-bold mb-4"
          variants={fadeInUp}
          initial="hidden"
          animate={isVideoLoaded ? "visible" : "hidden"}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          Unlock Your Mind&apos;s Potential
        </motion.h1>
        <motion.p 
          className="text-xl md:text-2xl lg:text-3xl mb-8 max-w-2xl"
          variants={fadeInUp}
          initial="hidden"
          animate={isVideoLoaded ? "visible" : "hidden"}
          transition={{ duration: 0.8, delay: 0.4 }}
        >
          Master Abacus, English, and Hindi with Speedy Scholars
        </motion.p>
        <motion.div
          variants={fadeInUp}
          initial="hidden"
          animate={isVideoLoaded ? "visible" : "hidden"}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <Button
            asChild
            className="bg-[#F5F5DC] text-black hover:bg-[#E6E6CA] text-lg px-8 py-6 rounded-full transition-all duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg"
          >
            <Link href={whatsappLink} target="_blank" rel="noopener noreferrer">
              Start Your Learning Journey
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="ml-2 h-5 w-5"
              >
                <line x1="5" y1="12" x2="19" y2="12" />
                <polyline points="12 5 19 12 12 19" />
              </svg>
            </Link>
          </Button>
        </motion.div>
      </div>

      {/* Animated Abacus Beads */}
      <div className="absolute bottom-0 left-0 w-full h-16 flex justify-around items-end overflow-hidden">
        {[...Array(10)].map((_, index) => (
          <motion.div
            key={index}
            className="w-4 h-16 bg-[#F5F5DC] rounded-full"
            initial={{ y: 100, opacity: 0 }}
            animate={{ 
              y: [0, Math.sin(index) * 20, 0],
              opacity: isVideoLoaded ? 0.7 : 0
            }}
            transition={{
              y: {
                repeat: Infinity,
                duration: 2,
                ease: "easeInOut",
                delay: index * 0.1
              },
              opacity: { duration: 1, delay: 1 + index * 0.1 }
            }}
          />
        ))}
      </div>
    </section>
  )
}