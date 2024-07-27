// src/test/Company.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import CompanyList from '../components/CompanyList';
import axios from '../axios';

jest.mock('../axios', () => {
  return {
    get: jest.fn(),
  };
});

test('renders CompanyList and checks for a company name', async () => {
  const companies = [
    { company_id: 1, name: 'Company A', address: '123 Main St', latitude: 40.7128, longitude: -74.0060 },
    { company_id: 2, name: 'Company B', address: '456 Elm St', latitude: 34.0522, longitude: -118.2437 },
  ];

  axios.get.mockResolvedValueOnce({ data: companies });

  render(
    <MemoryRouter>
      <CompanyList />
    </MemoryRouter>
  );

  const companyA = await screen.findByText(/Company A/i);
  const companyB = await screen.findByText(/Company B/i);

  expect(companyA).toBeInTheDocument();
  expect(companyB).toBeInTheDocument();
});
