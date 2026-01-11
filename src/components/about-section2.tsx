"use client"

import { motion, useAnimation } from 'framer-motion'
import { Button } from "@/components/ui/button"
import Link from 'next/link'
import { useEffect } from 'react'
import { useInView } from 'react-intersection-observer'

const AbacusAnimation = () => {
  return (
    <svg className="w-full h-48" viewBox="0 0 400 200">
      <motion.g
        animate={{
          x: [0, 20, 0],
          y: [0, 10, 0],
        }}
        transition={{
          repeat: Infinity,
          duration: 5,
          ease: "easeInOut",
        }}
      >
        {[0, 1, 2, 3, 4].map((row) => (
          <g key={row}>
            <line x1="50" y1={40 + row * 30} x2="350" y2={40 + row * 30} stroke="#8B4513" strokeWidth="4" />
            {[0, 1, 2, 3, 4, 5].map((col) => (
              <motion.circle
                key={`${row}-${col}`}
                cx={75 + col * 50}
                cy={40 + row * 30}
                r="15"
                fill="#F5F5DC"
                stroke="#8B4513"
                strokeWidth="2"
                animate={{
                  x: [0, (Math.random() - 0.5) * 30, 0],
                }}
                transition={{
                  repeat: Infinity,
                  duration: 3 + Math.random() * 2,
                  ease: "easeInOut",
                }}
              />
            ))}
          </g>
        ))}
      </motion.g>
    </svg>
  )
}

export default function AboutSection() {
  const controls = useAnimation()
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.1,
  })

  useEffect(() => {
    if (inView) {
      controls.start('visible')
    }
  }, [controls, inView])

  const containerVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.8,
        staggerChildren: 0.2,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 },
  }

  return (
    <section className="py-16 px-4 md:px-8 lg:px-16 bg-gradient-to-br from-white to-[#F5F5DC]">
      <motion.div
        ref={ref}
        variants={containerVariants}
        initial="hidden"
        animate={controls}
        className="max-w-7xl mx-auto"
      >
        <motion.h2 variants={itemVariants} className="text-3xl md:text-4xl font-bold text-center mb-8">
          We Are SPEEDY SCHOLARS
        </motion.h2>
        
        <motion.div variants={itemVariants} className="mb-12">
          <h3 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-4 text-center">
            UNLOCK THE POWER OF YOUR MIND
          </h3>
          <p className="text-xl md:text-2xl text-center text-gray-700">
            Precision, Speed, and Fun with Abacus
          </p>
        </motion.div>
        
        <motion.div variants={itemVariants} className="mb-12">
          <AbacusAnimation />
        </motion.div>
        
        <motion.p variants={itemVariants} className="text-lg text-center max-w-3xl mx-auto mb-8">
          At Speedy Scholars, we boost your child&apos;s mental arithmetic skills, turning
          math into a fun and engaging activity. We enhance concentration and memory,
          increasing confidence and paving the way to academic success.
        </motion.p>
        
        <motion.div variants={itemVariants} className="flex justify-center mb-12">
          <Button asChild className="bg-[#F5F5DC] text-black hover:bg-[#E6E6CA] transform hover:scale-105 transition-transform">
            <Link href="/about">
              Discover Our Method
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
                className="ml-2 h-4 w-4"
              >
                <line x1="5" y1="12" x2="19" y2="12" />
                <polyline points="12 5 19 12 12 19" />
              </svg>
            </Link>
          </Button>
        </motion.div>
        
        
      </motion.div>
    </section>
  )
}