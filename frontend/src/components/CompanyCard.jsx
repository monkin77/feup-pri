import React, { useState } from "react";
import { Grid, Rating, Tooltip, Typography } from "@mui/material";

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

    return (
        <div
            style={styles.cardContainer(isHover)}
            key={cardIdx}
            onClick={() => {
                console.log("Clicked container " + cardIdx);
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
                    <Typography style={styles.descriptionBig}>
                        IndWish Rating
                    </Typography>
                    <div style={styles.customRatingContainer}>
                        <Rating
                            name="custom-rating"
                            value={company.custom_rating}
                            precision={0.1}
                            readOnly
                        />

                        <Typography style={styles.description}>
                            ({company.custom_rating ?? "?"})
                        </Typography>
                    </div>

                    <div style={styles.divider} />

                    <Tooltip title="Calculated based on different Work Perks, such as Work/Life Balance">
                        <Typography style={styles.descriptionBig}>
                            Perks Rating
                        </Typography>
                    </Tooltip>
                    <div style={styles.customRatingContainer}>
                        <Rating
                            name="custom-rating"
                            value={avgPerksRating}
                            precision={0.1}
                            readOnly
                        />

                        <Typography style={styles.description}>
                            ({avgPerksRating ?? "?"})
                        </Typography>
                    </div>
                </Grid>
            </Grid>
        </div>
    );
};
