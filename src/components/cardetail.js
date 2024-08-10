import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const CarDetail = () => {
    const { id } = useParams();
    const [car, setCar] = useState(null);

    useEffect(() => {
        axios.get(`/api/cars/${id}/`)
            .then(response => {
                setCar(response.data);
            });
    }, [id]);

    if (!car) return <div>Loading...</div>;

    return (
        <div>
            <h1>{car.brand} {car.model}</h1>
            <p>{car.year}</p>
            <p>{car.price}</p>
            <p>{car.description}</p>
            <img src={car.image} alt={`${car.brand} ${car.model}`} />
        </div>
    );
};

export default CarDetail;