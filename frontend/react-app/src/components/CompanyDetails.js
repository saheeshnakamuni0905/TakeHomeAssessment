// src/components/CompanyDetails.js
import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from '../axios';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import CompanyChart from './CompanyChart';

function CompanyDetails() {
  const { id } = useParams();
  const [company, setCompany] = useState(null);
  const [locations, setLocations] = useState([]);
  const [chartData, setChartData] = useState({ labels: [], values: [] });
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`companies/${id}/`)
      .then(response => {
        setCompany(response.data);

        // Assuming the API returns these fields
        const { revenue, number_of_employees } = response.data;
        
        setChartData({
          labels: ['Revenue', 'Number of Employees'],
          values: [revenue, number_of_employees],
        });
      })
      .catch(error => console.error('Error fetching company details:', error));

    axios.get(`companies/${id}/locations/`)
      .then(response => setLocations(response.data))
      .catch(error => console.error('Error fetching locations:', error));
  }, [id]);

  if (!company) return <div>Loading...</div>;

  return (
    <div>
      <button onClick={() => navigate('/')}>Back to List</button>
      <h1>{company.name}</h1>
      <p>{company.address}</p>
      <ul>
        {locations.map(location => (
          <li key={location.location_id}>
            {location.name}: {location.address}
          </li>
        ))}
      </ul>
      <CompanyChart data={chartData} />
      <MapContainer center={[company.latitude, company.longitude]} zoom={13} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        <Marker position={[company.latitude, company.longitude]}>
          <Popup>{company.name}</Popup>
        </Marker>
        {locations.map(location => (
          <Marker key={location.location_id} position={[location.latitude, location.longitude]}>
            <Popup>{location.name}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default CompanyDetails;
