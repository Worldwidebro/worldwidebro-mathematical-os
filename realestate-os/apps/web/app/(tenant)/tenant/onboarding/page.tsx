'use client';

import { useState, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import Step1SetPassword from './step-1-set-password';
import Step2PaymentSetup from './step-2-payment-setup';
import Step3Complete from './step-3-complete';

function TenantOnboardingInner() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [currentStep, setCurrentStep] = useState(1);
  const [isLoading, setIsLoading] = useState(false);

  const email = searchParams.get('email') || '';
  const landlordName = searchParams.get('landlord') || 'Your Landlord';

  const handleNext = async () => {
    if (currentStep === 3) {
      setIsLoading(true);
      try {
        router.push('/tenant/portal');
      } catch (err) {
        console.error('Onboarding submission failed:', err);
      } finally {
        setIsLoading(false);
      }
    } else {
      setCurrentStep(currentStep + 1);
    }
  };

  const handleBack = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const progressPercentage = (currentStep / 3) * 100;

  return (
    <div className="min-h-screen bg-gray-950 py-12 px-4">
      <div className="mx-auto max-w-2xl">
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-3xl font-bold text-gray-100">Welcome</h1>
            <span className="text-sm font-medium text-gray-400">
              Step {currentStep} of 3
            </span>
          </div>
          <div className="w-full bg-gray-700 rounded-full h-2">
            <div
              className="bg-emerald-600 h-2 rounded-full transition-all"
              style={{ width: `${progressPercentage}%` }}
            />
          </div>
        </div>

        <div className="bg-gray-900 rounded-lg shadow-lg p-8 border border-gray-800">
          {currentStep === 1 && <Step1SetPassword email={email} />}
          {currentStep === 2 && <Step2PaymentSetup landlordName={landlordName} />}
          {currentStep === 3 && <Step3Complete />}

          <div className="flex gap-4 mt-8">
            <button
              onClick={handleBack}
              disabled={currentStep === 1 || isLoading}
              className="flex-1 px-4 py-2 border border-gray-700 rounded-lg font-medium text-gray-400 hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              Back
            </button>
            <button
              onClick={handleNext}
              disabled={isLoading}
              className="flex-1 px-4 py-2 bg-emerald-600 text-white rounded-lg font-medium hover:bg-emerald-700 disabled:bg-gray-700 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? 'Loading...' : currentStep === 3 ? 'Go to Portal' : 'Next'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function TenantOnboarding() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center bg-gray-950 text-gray-400">Loading onboarding...</div>}>
      <TenantOnboardingInner />
    </Suspense>
  );
}
