import React, { useState, useEffect } from "react";
import { CircularProgress, Typography } from "@mui/material";
import { useLocation } from "react-router-dom";
import { querySolr } from "../controller/solr.js";
import { CompanyCard } from "../components/CompanyCard.jsx";
import { CompanyDetails } from "../components/CompanyDetails.jsx";

const styles = {
    container: {
        padding: "1rem",
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
        position: "relative",
        minHeight: "100%",
    },
    loadingContainer: {
        display: "flex",
        flexDirection: "column",
        flex: 1,
        alignItems: "center",
        marginTop: "15%",
    },
    loading: {
        marginBottom: "2rem",
    },
    resultsContainer: {
        display: "flex",
        flexDirection: "row",
        flex: 1,
        minHeight: "100%",
    },
    cardsColumn: { width: "40%" },
    cardDetailsContainer: { width: "60%" },
    cardDetailsInner: { margin: 30 },
};

export const ResultsPage = () => {
    const location = useLocation();

    const { searchValue, fieldBoosts, numRows, queryOp, offset } =
        location.state;

    const [loading, setLoading] = useState(true);
    const [results, setResults] = useState({
        numFound: 0,
        docs: [],
        numFoundExact: false,
        start: 0,
    });
    const [selectedCard, setSelectedCard] = useState(null);

    useEffect(() => {
        const fetchResults = async () => {
            console.log("Fetching results for: " + searchValue);
            const res = await querySolr(
                searchValue,
                queryOp,
                fieldBoosts,
                numRows,
                offset
            );
            if (!res.ok) {
                console.log("Error fetching results: " + res);
            } else {
                setResults(res.data);
                setLoading(false);
                if (res.data.docs?.length > 0) {
                    setSelectedCard(0);
                }
            }
        };

        fetchResults();
    }, [searchValue, queryOp, fieldBoosts, numRows, offset]);

    return (
        <div style={styles.container}>
            {loading ? (
                <div style={styles.loadingContainer}>
                    <CircularProgress style={styles.loading} size={75} />
                    <Typography variant="h3">Loading...</Typography>
                </div>
            ) : (
                <>
                    <Typography variant="h4">
                        Found {results.numFound} results for: {searchValue}
                    </Typography>

                    <div style={styles.resultsContainer}>
                        <div style={styles.cardsColumn}>
                            {results.docs.map((document, index) => {
                                return (
                                    <CompanyCard
                                        company={document}
                                        cardIdx={index}
                                        selectCard={setSelectedCard}
                                        key={`card-${index}`}
                                    />
                                );
                            })}
                        </div>

                        <div style={styles.cardDetailsContainer}>
                            <div style={styles.cardDetailsInner}>
                                {selectedCard !== null && (
                                    <CompanyDetails
                                        company={results.docs[selectedCard]}
                                    />
                                )}
                            </div>
                        </div>
                    </div>
                </>
            )}
        </div>
    );
};
