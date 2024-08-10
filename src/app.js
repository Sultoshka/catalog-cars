import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import CarPage from './pages/CarPage';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={HomePage} />
                <Route path="/cars/:id" component={CarPage} />
            </Switch>
        </Router>
    );
}

export default App;
