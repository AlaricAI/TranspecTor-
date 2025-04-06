// Portfolio - Asadbek Qodirberganov

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Github, Mail } from "lucide-react";

export default function Portfolio() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-200 dark:from-slate-900 dark:to-slate-800 text-gray-800 dark:text-gray-100 p-6 max-w-5xl mx-auto space-y-14">

      {/* Hero Section */}
      <section className="text-center space-y-4">
        <h1 className="text-5xl font-extrabold tracking-tight text-indigo-600 dark:text-indigo-400">Asadbek Qodirberganov</h1>
        <p className="text-xl">AI Developer | Data Scientist | Physics & History Enthusiast 🤓</p>
        <div className="flex justify-center gap-4 mt-4">
          <Button variant="outline" asChild>
            <a href="https://github.com/asadbek" target="_blank">
              <Github className="w-5 h-5 mr-2" /> GitHub
            </a>
          </Button>
          <Button variant="outline" asChild>
            <a href="mailto:asadbek@example.com">
              <Mail className="w-5 h-5 mr-2" /> Email
            </a>
          </Button>
        </div>
      </section>

      {/* About Me */}
      <section className="space-y-4">
        <h2 className="text-3xl font-bold border-b border-gray-300 pb-2">About Me</h2>
        <p className="text-lg leading-relaxed">
          Men 16 yoshdaman va AI, Data Science hamda Fundamental Fizikaga qiziqaman. Mening asosiy maqsadim — sun’iy intellekt yordamida haqiqiy muammolarga yechim topish va bu sohada o‘z ismimni tarixga yozish. Hozirda mustaqil loyihalar va o‘quv kurslar orqali tajriba to‘plamoqdaman.
        </p>
      </section>

      {/* Projects */}
      <section className="space-y-6">
        <h2 className="text-3xl font-bold border-b border-gray-300 pb-2">Projects</h2>

        {/* Project Card 1 */}
        <Card className="shadow-lg hover:shadow-xl transition-shadow duration-300">
          <CardContent className="p-6 space-y-3">
            <h3 className="text-2xl font-semibold text-indigo-700 dark:text-indigo-300">AI Model for Handwritten Digit Recognition</h3>
            <p className="text-base">
              Bu loyiha MNIST dataset yordamida yaratilgan. Neural network yordamida raqamlarni aniqlash
              uchun Python va TensorFlow kutubxonalaridan foydalandim. Model ancha yaxshi aniqlik ko‘rsatdi.
            </p>
            <a
              href="https://github.com/asadbek/mnist-ai"
              target="_blank"
              className="text-indigo-600 dark:text-indigo-400 hover:underline"
            >
              GitHub Repository
            </a>
          </CardContent>
        </Card>

        {/* Project Card 2 */}
        <Card className="shadow-lg hover:shadow-xl transition-shadow duration-300">
          <CardContent className="p-6 space-y-3">
            <h3 className="text-2xl font-semibold text-emerald-700 dark:text-emerald-300">World Happiness Data Analysis</h3>
            <p className="text-base">
              Mohirdev kursi doirasida bajarilgan loyiha. Pandas va Matplotlib yordamida dunyo davlatlarining baxt indekslarini vizualizatsiya qilib, qiziqarli xulosalar chiqarildi.
            </p>
            <a
              href="https://github.com/asadbek/happiness-analysis"
              target="_blank"
              className="text-emerald-600 dark:text-emerald-400 hover:underline"
            >
              GitHub Repository
            </a>
          </CardContent>
        </Card>
      </section>

      {/* Contact */}
      <section className="space-y-4">
        <h2 className="text-3xl font-bold border-b border-gray-300 pb-2">Contact</h2>
        <p className="text-lg">Quyidagi manzillar orqali aloqaga chiqishingiz mumkin:</p>
        <ul className="list-disc list-inside space-y-1 text-base">
          <li>Email: asadbek@example.com</li>
          <li>GitHub: github.com/asadbek</li>
          <li>Telegram: @asadbek_ai</li>
        </ul>
      </section>

    </div>
  );
}
