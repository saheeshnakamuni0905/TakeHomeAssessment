module.exports = {
    setupFilesAfterEnv: ['<rootDir>/src/setupTests.js'],
    testEnvironment: 'jsdom',
    transform: {
      '^.+\\.(js|jsx)$': 'babel-jest',
    },
    transformIgnorePatterns: [
      'node_modules/(?!(axios|react-leaflet|leaflet)/)',
    ],
    moduleNameMapper: {
      '^axios$': '<rootDir>/src/axios',
    },
  };
  