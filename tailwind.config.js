/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./**/*.html",
    "./templates/*.html",
    "./templates/**/*.html",
    "./templates/**/**/*.html",
    "**/**/*.html",
    "**/**/forms.py",
    "tabnews/static/js/custom.js"
  ],
  theme: {
    extend: {
      colors: {
          'dark': 'rgb(22, 27, 34)',
          'darkMode': '#0d1117',
          'darkButton': 'rgb(48, 54, 61)',
          'darkInput': 'rgb(1, 4, 9)',
      }
    },
  },
  plugins: [],
}