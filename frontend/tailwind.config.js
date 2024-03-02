/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "background": "#D7CFBC",
        "placeholder": "#7D7D7D",
        "light": "#E1E1E1",
        "text": "#4E533F"
      },
      fontFamily: {
        "title": ["Gluten"],
      },
      fontWeight: {
        "title": 500
      },
      fontSize: {
        "title": ["7rem", {
          letterSpacing: "-0.01em"
        }],
        "subtitle": ["3rem"]
      }
    },
  },
  // eslint-disable-next-line no-undef
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        sprouts: {
          "primary": "#9FB783",
          "secondary": "#CBA3DD",
          "accent": "#37cdbe",
          "neutral": "#3d4451",
          "base-100": "#E1E1E1",

          "--rounded-box": "1.5rem", // border radius rounded-box utility class, used in card and other large boxes
          "--rounded-btn": "1.5rem", // border radius rounded-btn utility class, used in buttons and similar element
        }
      }
    ]
  }
}
