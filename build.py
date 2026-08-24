#!/usr/bin/env python3
# Composes the responsive, animated "Security Checkpoint" verification-gate SVG.
# All images base64-embedded (proxy strips external hrefs). Animations via SMIL+CSS.
cdc = open('b_cdc.txt').read().strip()
cro = open('b_cro.txt').read().strip()
qr  = open('b_qr.txt').read().strip()

SVG = r'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="100%" height="100%" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet"
     font-family="'Helvetica Neue', Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="900" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#eef3fb"/><stop offset="1" stop-color="#e4eaf6"/>
    </linearGradient>
    <radialGradient id="halo" cx="720" cy="120" r="620" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#dbe6ff" stop-opacity="0.9"/><stop offset="1" stop-color="#dbe6ff" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="brand" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2f7bff"/><stop offset="1" stop-color="#1657ff"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#22d3ee" stop-opacity="0"/>
      <stop offset="0.75" stop-color="#22d3ee" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#22d3ee" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="24" stdDeviation="34" flood-color="#26365f" flood-opacity="0.22"/>
    </filter>
    <filter id="navShadow" x="-5%" y="-40%" width="110%" height="220%">
      <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#26365f" flood-opacity="0.10"/>
    </filter>
    <clipPath id="scanClip"><rect x="592" y="336" width="256" height="256" rx="16"/></clipPath>
    <style>
      .t{fill:#0b1533}.m{fill:#6b7a99}
      @keyframes blink{0%,100%{opacity:1}50%{opacity:.25}}
      .live{animation:blink 1.6s ease-in-out infinite}
    </style>
  </defs>

  <!-- backdrop -->
  <rect x="-400" y="-300" width="2240" height="1500" fill="url(#bg)"/>
  <rect x="-400" y="-300" width="2240" height="1500" fill="url(#halo)"/>

  <!-- ================= NAVBAR ================= -->
  <g filter="url(#navShadow)">
    <rect x="0" y="0" width="1440" height="74" fill="#ffffff"/>
  </g>
  <rect x="0" y="73.5" width="1440" height="1" fill="#e6ecf7"/>
  <!-- brand -->
  <rect x="40" y="20" width="34" height="34" rx="9" fill="#0b1c4a"/>
  <image x="40" y="20" width="34" height="34" xlink:href="data:image/png;base64,__CDC__"/>
  <text x="86" y="44" class="t" font-size="21" font-weight="800" letter-spacing="-0.3">crypto.com</text>
  <!-- trust / address chip (always check crypto.com) -->
  <g transform="translate(610,19)">
    <rect x="0" y="0" width="224" height="36" rx="18" fill="#eefaf1" stroke="#bfe6c9" stroke-width="1"/>
    <circle cx="22" cy="18" r="8.5" fill="#16a34a"/>
    <path d="M18.5 18 l3 3 l5 -6" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M40 13 h5 v-2 a4 4 0 0 1 8 0 v2 h5 v10 h-18 z" fill="none" stroke="#15803d" stroke-width="1.6"/>
    <text x="62" y="23" fill="#15803d" font-size="14.5" font-weight="700">crypto.com</text>
    <text x="150" y="23" fill="#4f9a63" font-size="13" font-weight="600">Secure</text>
  </g>
  <!-- nav links -->
  <g font-size="15" font-weight="600" class="m">
    <text x="1028" y="45">Buy Crypto</text>
    <text x="1140" y="45">Exchange</text>
    <text x="1240" y="45">Wallet</text>
  </g>
  <circle cx="1388" cy="37" r="16" fill="#e8edf7"/>
  <circle cx="1388" cy="31" r="6" fill="#9fb0cf"/>
  <path d="M1376 50 a12 11 0 0 1 24 0 z" fill="#9fb0cf"/>

  <!-- ================= CARD ================= -->
  <g filter="url(#cardShadow)">
    <rect x="440" y="132" width="560" height="656" rx="30" fill="#ffffff"/>
  </g>

  <!-- checkpoint pill -->
  <g transform="translate(608,168)">
    <rect x="0" y="0" width="224" height="34" rx="17" fill="#eaf1ff"/>
    <path d="M16 8 l9 -3 l9 3 v6 c0 6 -4 10 -9 12 c-5 -2 -9 -6 -9 -12 z" fill="none" stroke="#1657ff" stroke-width="1.7"/>
    <path d="M17 15 l3 3 l6 -7" stroke="#1657ff" stroke-width="1.7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="40" y="22" fill="#1657ff" font-size="13" font-weight="800" letter-spacing="1.5">SECURITY CHECKPOINT</text>
  </g>

  <!-- title + subtitle -->
  <text x="720" y="252" class="t" font-size="34" font-weight="800" text-anchor="middle" letter-spacing="-0.5">Verify it&#8217;s you to continue</text>
  <text x="720" y="290" class="m" font-size="17" text-anchor="middle">Scan the QR code with the Crypto.com App to confirm it&#8217;s you.</text>
  <text x="720" y="314" class="m" font-size="17" text-anchor="middle">Your <tspan fill="#0b1533" font-weight="700">5,000 CRO</tspan> reward is reserved until verification completes.</text>

  <!-- ===== QR scanner ===== -->
  <rect x="588" y="332" width="264" height="264" rx="20" fill="#f7f9fd" stroke="#e6ecf7" stroke-width="1.5"/>
  <image x="605" y="349" width="230" height="230" xlink:href="data:image/png;base64,__QR__"/>

  <!-- sweeping scan beam (clipped to QR) -->
  <g clip-path="url(#scanClip)">
    <rect x="592" y="336" width="256" height="46" fill="url(#beam)">
      <animate attributeName="y" values="336;546;336" keyTimes="0;0.5;1" dur="2.6s" repeatCount="indefinite"/>
    </rect>
    <rect x="592" y="380" width="256" height="2.5" fill="#22d3ee">
      <animate attributeName="y" values="380;590;380" keyTimes="0;0.5;1" dur="2.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;1;0.9" dur="1.3s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- rotating shiny border: base ring + orbiting bright segment -->
  <rect x="588" y="332" width="264" height="264" rx="20" fill="none" stroke="#dbe7ff" stroke-width="3"/>
  <rect x="588" y="332" width="264" height="264" rx="20" fill="none" stroke="#38bdf8" stroke-opacity="0.25" stroke-width="7"
        stroke-linecap="round" stroke-dasharray="150 2050">
    <animate attributeName="stroke-dashoffset" values="0;-2200" dur="3s" repeatCount="indefinite"/>
  </rect>
  <rect x="588" y="332" width="264" height="264" rx="20" fill="none" stroke="url(#brand)" stroke-width="3.5"
        stroke-linecap="round" stroke-dasharray="150 2050">
    <animate attributeName="stroke-dashoffset" values="0;-2200" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- corner brackets -->
  <g stroke="#1657ff" stroke-width="3.5" fill="none" stroke-linecap="round">
    <path d="M604 356 v-14 h14"/><path d="M836 356 v-14 h-14"/>
    <path d="M604 572 v14 h14"/><path d="M836 572 v14 h-14"/>
    <animate attributeName="opacity" values="1;0.45;1" dur="2.6s" repeatCount="indefinite"/>
  </g>

  <!-- Cronos reserved chip -->
  <g transform="translate(560,622)">
    <rect x="0" y="0" width="320" height="46" rx="23" fill="#f4f7fe" stroke="#e2e9f7" stroke-width="1"/>
    <circle cx="27" cy="23" r="16" fill="#0b1c4a"/>
    <image x="11" y="7" width="32" height="32" xlink:href="data:image/png;base64,__CRO__"/>
    <text x="54" y="28" class="t" font-size="15" font-weight="700">5,000 CRO reserved</text>
    <circle cx="228" cy="23" r="3" fill="#f59e0b" class="live"/>
    <text x="240" y="28" fill="#b4791a" font-size="14" font-weight="700">09:57</text>
  </g>

  <!-- locked continue button (scan-to-proceed gate) -->
  <g transform="translate(490,690)">
    <rect x="0" y="0" width="460" height="56" rx="15" fill="#eef1f6" stroke="#e0e5ee" stroke-width="1"/>
    <path d="M104 26 h5 v-4 a5 5 0 0 1 10 0 v4 h5 v13 h-20 z" fill="none" stroke="#98a4bd" stroke-width="2"/>
    <text x="134" y="35" fill="#98a4bd" font-size="16.5" font-weight="700" text-anchor="start">Complete scan to continue</text>
  </g>

  <!-- trust row -->
  <g transform="translate(720,768)" text-anchor="middle">
    <text x="0" y="0" class="m" font-size="13.5">
      <tspan font-weight="700" fill="#6b7a99">&#128274; TLS secured</tspan>
      <tspan dx="6">&#183;  Verified by crypto.com  &#183;  256-bit encryption</tspan>
    </text>
  </g>

  <!-- footer PoC marker -->
  <text x="720" y="838" fill="#8493b3" font-size="13.5" text-anchor="middle">
    Security PoC by 0xazanul &#183; rendered on the trusted crypto.com origin via /cdn-cgi/image open proxy &#183; HackerOne
  </text>
</svg>
'''
SVG = SVG.replace('__CDC__', cdc).replace('__CRO__', cro).replace('__QR__', qr)
open('secure0x.svg', 'w').write(SVG)
print('wrote secure0x.svg', len(SVG), 'bytes')
