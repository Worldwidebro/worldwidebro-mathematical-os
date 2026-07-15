import Navbar from '../components/Navbar';
import HeroSection from '../components/HeroSection';
import InfoSection from '../components/InfoSection';
import BackedBySection from '../components/BackedBySection';
import UseCasesSection from '../components/UseCasesSection';
import Footer from '../components/Footer';

export default function HomePage() {
  return (
    <div className="flex flex-col bg-[#F5F5F5]">
      <div className="h-screen flex flex-col overflow-hidden">
        <Navbar />
        <HeroSection />
      </div>

      <InfoSection />
      <BackedBySection />
      <UseCasesSection />
      <Footer />
    </div>
  );
}
