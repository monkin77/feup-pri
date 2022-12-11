import React from "react";
import { Rating, Tooltip, Typography } from "@mui/material";

const styles = {
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
};

export const RatingComponent = ({
    rating,
    precision = 0.1,
    title,
    hasTooltip,
    tooltipText,
}) => {
    return (
        <>
            {hasTooltip ? (
                <Tooltip title={tooltipText}>
                    <Typography style={styles.descriptionBig}>
                        {title}
                    </Typography>
                </Tooltip>
            ) : (
                <Typography style={styles.descriptionBig}>{title}</Typography>
            )}

            <div style={styles.customRatingContainer}>
                <Rating
                    name="custom-rating"
                    value={rating}
                    precision={precision}
                    readOnly
                />

                <Typography style={styles.description}>
                    ({rating ?? "?"})
                </Typography>
            </div>
        </>
    );
};
