import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const CarList = () => {
    const [cars, setCars] = useState([]);

    useEffect(() => {
        axios.get('/api/cars/')
            .then(response => {
                setCars(response.data);
            });
    }, []);

    return (
        <div>
            <h1>Car List</h1>
            <ul>
                {cars.map(car => (
                    <li key={car.id}>
                        <Link to={`/cars/${car.id}`}>{car.brand} {car.model}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CarList;
