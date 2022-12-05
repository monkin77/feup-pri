import React, { useState, useEffect } from "react";
import { CircularProgress, Typography } from "@mui/material";
import { useLocation } from "react-router-dom";
import {querySolr} from '../controller/solr.js';

const styles = {
    container: {
        padding: "1rem",
        minHeight: "100vh",
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
        position: "relative",
        height: "100%",
    },
    results: {
        display: "flex",
        flexDirection: "column",
        flex: 1,
        height: "100%",
        justifyContent: "center",
        alignItems: "center",
    },
    loading: {
        marginBottom: "2rem",
    }
};

export const ResultsPage = () => {
    const location = useLocation();
    const searchValue = location.state?.searchValue;

    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // TODO: Fetch items from the backend for this search
        fetchResults();
    }, []);

    const fetchResults = async () => {
        console.log("Fetching results for: " + searchValue);
        const res = await querySolr(searchValue);
        console.log(res);
        setLoading(false);
    }

    return (
        <div style={styles.container}>
            <Typography variant="h4">Showing Results for: {searchValue}</Typography>
           
            {loading ? 
                    <div style={styles.results}>
                        <CircularProgress style={styles.loading} size={75} /> 
                        <Typography variant="h3">Loading...</Typography>
                    </div> : (
                <div> 
                    <Typography variant="h5">Results</Typography>
                </div>
            )}
        </div>
    );
};
