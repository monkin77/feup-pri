// Create a Navbar component
import { Divider, Typography } from '@mui/material';
import { grey } from '@mui/material/colors';
import React from 'react';
import { Link } from 'react-router-dom';


const styles = {
    container: {
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
        position: "absolute",
        top: 0,
        right: 0,
        marginRight: "20rem",
        marginTop: "2rem",
    },
    link: {
        textDecoration: "none",
        color: grey[800],
    },
    navbar: {
        display: "flex",
        justifyContent: "flex-end"
    },
    divider: {
        margin: 10,
        borderRightWidth: 2,
        height: "1rem",
    },
};

export const Navbar = () => {
    return (
        <div style={styles.container}>
            <nav style={styles.navbar}>
                <Link style={styles.link} className="navbar-brand" to="/">
                    <Typography variant="h5">
                        Home
                    </Typography>
                </Link>

                <Divider style={styles.divider} orientation="vertical" flexItem />

                <Link style={styles.link} className="navbar-brand" to="/about">
                    <Typography variant="h5">
                        About
                    </Typography>
                </Link>
            </nav>
        </div>
    );
};