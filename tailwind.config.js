/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",
    "./templates/*.html",
    "./templates/**/*.html",
    "./templates/**/**/*.html",
    "**/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
          'dark': '#1f2328',
      }
    },
  },
  plugins: [],
}