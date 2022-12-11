import React from "react";
import { Typography } from "@mui/material";

const styles = {
    container: {
        width: "100%",
        borderRadius: 15,
        border: "solid",
        borderWidth: 1,
        minHeight: "100%",
        padding: 10,
    },
    title: {
        fontSize: 22,
        fontWeight: "bold",
    },
    descriptionBig: {
        fontSize: 20,
    },
    description: {
        fontSize: 15,
    },
    customRatingContainer: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
    },
    divider: {
        height: 10,
    },
};

export const CompanyDetails = ({ company }) => {
    return (
        <div style={styles.container}>
            <Typography style={styles.title}>{company.name}</Typography>
        </div>
    );
};
