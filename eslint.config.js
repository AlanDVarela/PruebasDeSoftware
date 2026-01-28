module.exports = [
  {
    // Aplica a todos los archivos JS
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "commonjs",
    },
    rules: {
      // Permitir console.log para el Hola Mundo
      "no-console": "off",
    },
  },
];
