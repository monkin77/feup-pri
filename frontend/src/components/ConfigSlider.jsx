import { Slider, Typography } from "@mui/material";
import React from "react";

const styles = {
    configField: {
        display: "flex",
        flexDirection: "row",
        marginTop: 15,
    },
    configSlider: {
        marginLeft: 20,
        marginRight: 20,
    },
    title: {
        minWidth: 120,
    },
};

export const ConfigSlider = ({
    title,
    field,
    fieldKey,
    onChange,
    min,
    max,
    step,
}) => {
    return (
        <div style={styles.configField}>
            <Typography style={styles.title}>{title}</Typography>
            <Slider
                aria-label="nameBoost"
                value={field}
                onChange={(_, newVal) => onChange(fieldKey, newVal)}
                valueLabelDisplay="auto"
                step={step}
                marks
                min={min}
                max={max}
                style={styles.configSlider}
            />
        </div>
    );
};
