import { useState } from 'react'
import Navbar from './components/Navbar'
import MobileMenu from './components/MobileMenu'
import Hero from './components/Hero'

const VIDEO_URL =
  'https://d8j0ntlcm91z4.cloudfront.net/user_38xzZboKViGWJOttwIXH07lWA1P/hf_20260622_204221_5339e40b-e73d-4ab0-9c65-79c18c66fd50.mp4'

export default function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="relative h-screen w-full overflow-hidden bg-black font-geist">
      <video
        autoPlay
        muted
        loop
        playsInline
        className="absolute h-full w-full object-cover"
        style={{ objectPosition: '70% center' }}
        src={VIDEO_URL}
      />

      <Navbar mobileMenuOpen={mobileMenuOpen} setMobileMenuOpen={setMobileMenuOpen} />
      <MobileMenu mobileMenuOpen={mobileMenuOpen} setMobileMenuOpen={setMobileMenuOpen} />
      <Hero />
    </div>
  )
}
