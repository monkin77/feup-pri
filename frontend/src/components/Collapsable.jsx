import React from "react";
import {
    Accordion,
    AccordionDetails,
    AccordionSummary,
    Typography,
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const styles = {
    accordionContainer: {
        backgroundColor: "transparent",
        boxShadow: "none",
        padding: 0,
    },
    title: {
        fontSize: 22,
        fontWeight: "bold",
    },
};

export const Collapsable = ({ title, children, startOpen = true }) => {
    return (
        <Accordion
            style={styles.accordionContainer}
            TransitionProps={{ unmountOnExit: true }}
            defaultExpanded={startOpen}
        >
            <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
            >
                <Typography style={styles.title}>{title}</Typography>
            </AccordionSummary>
            <AccordionDetails>{children}</AccordionDetails>
        </Accordion>
    );
};
