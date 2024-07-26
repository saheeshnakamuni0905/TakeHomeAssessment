import React, { useEffect, useState } from 'react';
import axios from '../axios';
import { Link } from 'react-router-dom';

function CompanyList() {
  const [companies, setCompanies] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    axios.get('companies/')
      .then(response => setCompanies(response.data))
      .catch(error => console.error('Error fetching companies:', error));
  }, []);

  const handleSearch = event => {
    setSearchTerm(event.target.value);
  };

  const filteredCompanies = companies.filter(company =>
    company.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h1>Companies</h1>
      <input
        type="text"
        placeholder="Search companies"
        value={searchTerm}
        onChange={handleSearch}
      />
      <ul>
        {filteredCompanies.map(company => (
          <li key={company.company_id}>
            <Link to={`/company/${company.company_id}`}>{company.name}</Link>
            <p>{company.address}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CompanyList;
