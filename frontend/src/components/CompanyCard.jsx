import React, { useState } from "react";
import { Grid, Typography } from "@mui/material";
import { RatingComponent } from "./RatingComponent";

const styles = {
    cardContainer: (isHover) => ({
        width: "100%",
        height: 150,
        marginTop: 30,
        borderRadius: 15,
        border: "solid",
        borderWidth: 2,
        padding: 10,
        boxSizing: "border-box", // Make Card dimensions include the padding + margin
        ...(isHover && { cursor: "pointer", backgroundColor: "lightCyan" }),
    }),
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

export const CompanyCard = ({ company, cardIdx, selectCard }) => {
    const [isHover, setIsHover] = useState(false);

    // Calculate the average rating of all perks
    const perksRatings = Object.keys(company).filter((key) =>
        key.startsWith("ratings.")
    );
    let avgPerksRating = perksRatings.reduce(
        (accumulator, currPerk) => accumulator + company[currPerk],
        0
    );
    avgPerksRating = avgPerksRating / perksRatings.length;
    avgPerksRating = avgPerksRating.toFixed(2);
    if (avgPerksRating === "NaN") avgPerksRating = null;

    return (
        <div
            style={styles.cardContainer(isHover)}
            key={cardIdx}
            onClick={() => {
                selectCard(cardIdx);
            }}
            onMouseEnter={() => setIsHover(true)}
            onMouseLeave={() => setIsHover(false)}
        >
            <Grid container>
                <Grid item xs={8}>
                    <Typography style={styles.title}>{company.name}</Typography>

                    <Typography style={styles.description}>
                        Based on {company.reviews} reviews
                    </Typography>

                    <Typography style={styles.description}>
                        Industry: {company.industry}
                    </Typography>

                    <Typography style={styles.description}>
                        CEO Approval:{" "}
                        {company["ceo.approval"]
                            ? company["ceo.approval"] + "%"
                            : "?"}
                    </Typography>
                </Grid>

                <Grid item xs={4}>
                    <RatingComponent
                        rating={company.custom_rating}
                        precision={0.1}
                        title="IndWish Rating"
                        hasTooltip={true}
                        tooltipText="This rating is based on the global rating, happiness and perks parameters."
                    />

                    <div style={styles.divider} />

                    <RatingComponent
                        rating={avgPerksRating}
                        precision={0.1}
                        title="Perks Rating"
                        hasTooltip={true}
                        tooltipText="Calculated based on different Work Perks, such as Work/Life Balance"
                    />
                </Grid>
            </Grid>
        </div>
    );
};
