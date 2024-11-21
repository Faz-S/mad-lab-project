/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}", 
    "./<custom-directory>/**/*.{js,jsx,ts,tsx}",
    "./screens/**/*.{js,jsx,ts,tsx}", // Include screens folder
    "./components/**/*.{js,jsx,ts,tsx}", // Include components folder
    "./navigation/**/*.{js,jsx,ts,tsx}", // Include navigation folder
    "./assets/**/*.{js,jsx,ts,tsx}", // If you use JS/TS in assets
  ],
  theme: {
    extend: {
      colors: {
        primary: "#000",
        secondary: "#f1c40f",
        tertiary: "#fff6e7",
        quaternary: "#2ecc71",
        purple: "#000",
        grey: "#333333",
        lightblack: "#1E1E1E",
        blue: "#000",
      },
      spacing: {
        12: "3rem",
      },
      maxWidth: {
        1080: "1080px",
      },
      minHeight: {
        720: "720px",
      },
      borderRadius: {
        "2xl": "2rem",
      },
      fontSize: {
        "2xl": "2rem",
      },
      lineHeight: {
        12: "1.5",
      },
      letterSpacing: {
        "-1": "-0.1em",
      },
    },
  },
  plugins: [],
};
