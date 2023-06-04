/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./**/*.html",
    "./templates/*.html",
    "./templates/**/*.html",
    "./templates/**/**/*.html",
    "**/**/*.html",
    "**/**/*.py",
    "tabnews/static/js/custom.js"
  ],
  theme: {
    extend: {
      colors: {
          'dark': '#1f2328',
          'darkMode': '#0d1117',
      }
    },
  },
  plugins: [],
}