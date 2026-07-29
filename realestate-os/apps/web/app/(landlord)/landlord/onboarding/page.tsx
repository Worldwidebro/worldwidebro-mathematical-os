'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Step1Profile from './step-1-profile';
import Step2Properties from './step-2-properties';
import Step3Tenants from './step-3-tenants';
import Step4Complete from './step-4-complete';
import type { LandlordOnboardingData } from '@realestate-os/shared-types';

const STORAGE_KEY = 'landlord-onboarding';

const initialData: LandlordOnboardingData = {
  step1: { fullName: '', phone: '', company: '' },
  step2: { properties: [] },
  step3: { tenants: [] },
};

export default function LandlordOnboarding() {
  const router = useRouter();
  const [currentStep, setCurrentStep] = useState(1);
  const [data, setData] = useState<LandlordOnboardingData>(initialData);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        setData(parsed);
      } catch (err) {
        console.error('Failed to load saved onboarding data');
      }
    }
  }, []);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }, [data]);

  const handleNext = async () => {
    if (currentStep === 4) {
      setIsLoading(true);
      try {
        console.log('Submitting onboarding data:', data);
        localStorage.removeItem(STORAGE_KEY);
        router.push('/landlord/dashboard');
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

  const handleUpdateData = (updates: Partial<LandlordOnboardingData>) => {
    setData((prev) => ({ ...prev, ...updates }));
  };

  const progressPercentage = (currentStep / 4) * 100;

  return (
    <div className="min-h-screen bg-gray-950 py-12 px-4">
      <div className="mx-auto max-w-2xl">
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h1 className="text-3xl font-bold text-gray-100">Complete Your Setup</h1>
            <span className="text-sm font-medium text-gray-400">
              Step {currentStep} of 4
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
          {currentStep === 1 && (
            <Step1Profile
              data={data.step1}
              onUpdate={(step1) => handleUpdateData({ step1 })}
            />
          )}
          {currentStep === 2 && (
            <Step2Properties
              data={data.step2}
              onUpdate={(step2) => handleUpdateData({ step2 })}
            />
          )}
          {currentStep === 3 && (
            <Step3Tenants
              data={data.step3}
              onUpdate={(step3) => handleUpdateData({ step3 })}
            />
          )}
          {currentStep === 4 && <Step4Complete />}

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
              {isLoading ? 'Loading...' : currentStep === 4 ? 'Complete Setup' : 'Next'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
