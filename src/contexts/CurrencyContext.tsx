"use client"

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

// Exchange rates (approximate - you can update these periodically)
// Base currency is INR
const EXCHANGE_RATES: Record<string, number> = {
  INR: 1,
  USD: 0.012,    // 1 INR = 0.012 USD (approx)
  GBP: 0.0095,   // 1 INR = 0.0095 GBP (approx)
  EUR: 0.011,    // 1 INR = 0.011 EUR (approx)
  AUD: 0.018,    // 1 INR = 0.018 AUD (approx)
  CAD: 0.016,    // 1 INR = 0.016 CAD (approx)
  NZD: 0.020,    // 1 INR = 0.020 NZD (approx)
  AED: 0.044,    // 1 INR = 0.044 AED (approx)
  SGD: 0.016,    // 1 INR = 0.016 SGD (approx)
};

const CURRENCY_SYMBOLS: Record<string, string> = {
  INR: '₹',
  USD: '$',
  GBP: '£',
  EUR: '€',
  AUD: 'A$',
  CAD: 'C$',
  NZD: 'NZ$',
  AED: 'AED ',
  SGD: 'S$',
};

const CURRENCY_NAMES: Record<string, string> = {
  INR: 'Indian Rupee',
  USD: 'US Dollar',
  GBP: 'British Pound',
  EUR: 'Euro',
  AUD: 'Australian Dollar',
  CAD: 'Canadian Dollar',
  NZD: 'New Zealand Dollar',
  AED: 'UAE Dirham',
  SGD: 'Singapore Dollar',
};

// Country to currency mapping
const COUNTRY_CURRENCY: Record<string, string> = {
  IN: 'INR',
  US: 'USD',
  GB: 'GBP',
  UK: 'GBP',
  DE: 'EUR',
  FR: 'EUR',
  IT: 'EUR',
  ES: 'EUR',
  NL: 'EUR',
  BE: 'EUR',
  AT: 'EUR',
  IE: 'EUR',
  PT: 'EUR',
  AU: 'AUD',
  CA: 'CAD',
  NZ: 'NZD',
  AE: 'AED',
  SG: 'SGD',
};

interface CurrencyContextType {
  currency: string;
  setCurrency: (currency: string) => void;
  formatPrice: (priceInINR: number) => string;
  symbol: string;
  currencyName: string;
  isLoading: boolean;
  availableCurrencies: string[];
}

const CurrencyContext = createContext<CurrencyContextType | undefined>(undefined);

export function CurrencyProvider({ children }: { children: ReactNode }) {
  const [currency, setCurrency] = useState('INR');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Try to detect user's country from various sources
    const detectCurrency = async () => {
      try {
        // First, check if user has a saved preference
        const savedCurrency = localStorage.getItem('preferredCurrency');
        if (savedCurrency && EXCHANGE_RATES[savedCurrency]) {
          setCurrency(savedCurrency);
          setIsLoading(false);
          return;
        }

        // Try to get location from IP using a free geolocation API
        const response = await fetch('https://ipapi.co/json/', {
          signal: AbortSignal.timeout(3000) // 3 second timeout
        });

        if (response.ok) {
          const data = await response.json();
          const countryCode = data.country_code;
          const detectedCurrency = COUNTRY_CURRENCY[countryCode] || 'INR';
          setCurrency(detectedCurrency);
          localStorage.setItem('preferredCurrency', detectedCurrency);
        }
      } catch {
        // If geolocation fails, try browser's timezone/locale
        try {
          const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
          if (timezone.includes('America/New_York') || timezone.includes('America/Los_Angeles') || timezone.includes('America/Chicago')) {
            setCurrency('USD');
          } else if (timezone.includes('Europe/London')) {
            setCurrency('GBP');
          } else if (timezone.includes('Europe/')) {
            setCurrency('EUR');
          } else if (timezone.includes('Australia/')) {
            setCurrency('AUD');
          } else if (timezone.includes('Asia/Kolkata') || timezone.includes('Asia/Calcutta')) {
            setCurrency('INR');
          }
        } catch {
          // Fallback to INR
          setCurrency('INR');
        }
      } finally {
        setIsLoading(false);
      }
    };

    detectCurrency();
  }, []);

  const handleSetCurrency = (newCurrency: string) => {
    if (EXCHANGE_RATES[newCurrency]) {
      setCurrency(newCurrency);
      localStorage.setItem('preferredCurrency', newCurrency);
    }
  };

  const formatPrice = (priceInINR: number): string => {
    const rate = EXCHANGE_RATES[currency] || 1;
    const convertedPrice = priceInINR * rate;
    const symbol = CURRENCY_SYMBOLS[currency] || '₹';

    // Round to appropriate decimal places
    let formattedPrice: string;
    if (currency === 'INR') {
      // For INR, use Indian number formatting
      formattedPrice = convertedPrice.toLocaleString('en-IN', {
        maximumFractionDigits: 0,
      });
    } else {
      // For other currencies, round to nearest whole number or 2 decimal places
      if (convertedPrice >= 10) {
        formattedPrice = Math.round(convertedPrice).toLocaleString('en-US');
      } else {
        formattedPrice = convertedPrice.toFixed(2);
      }
    }

    return `${symbol}${formattedPrice}`;
  };

  return (
    <CurrencyContext.Provider
      value={{
        currency,
        setCurrency: handleSetCurrency,
        formatPrice,
        symbol: CURRENCY_SYMBOLS[currency] || '₹',
        currencyName: CURRENCY_NAMES[currency] || 'Indian Rupee',
        isLoading,
        availableCurrencies: Object.keys(EXCHANGE_RATES),
      }}
    >
      {children}
    </CurrencyContext.Provider>
  );
}

export function useCurrency() {
  const context = useContext(CurrencyContext);
  if (context === undefined) {
    throw new Error('useCurrency must be used within a CurrencyProvider');
  }
  return context;
}

// Currency selector component
export function CurrencySelector({ className = '' }: { className?: string }) {
  const { currency, setCurrency, availableCurrencies } = useCurrency();

  return (
    <select
      value={currency}
      onChange={(e) => setCurrency(e.target.value)}
      className={`bg-white border border-gray-300 rounded-lg px-3 py-2 text-sm font-medium text-gray-700 hover:border-[#8B6F47] focus:outline-none focus:ring-2 focus:ring-[#8B6F47] focus:border-transparent cursor-pointer ${className}`}
    >
      {availableCurrencies.map((curr) => (
        <option key={curr} value={curr}>
          {CURRENCY_SYMBOLS[curr]} {curr}
        </option>
      ))}
    </select>
  );
}
