import React from "react";
import { Divider, Grid, Typography } from "@mui/material";
import { RatingComponent } from "./RatingComponent";
import { getHappinessRatings, getPerksRatings } from "../utils/utils";
import { Collapsable } from "./Collapsable";

const styles = {
    container: {
        width: "100%",
        borderRadius: 15,
        border: "solid",
        borderWidth: 1,
        minHeight: "20vh",
        padding: 10,
    },
    mainTitle: {
        fontSize: 25,
        fontWeight: "bold",
    },
    title: {
        fontSize: 22,
        fontWeight: "bold",
    },
    titleXS: {
        fontSize: 20,
        fontWeight: "bold",
    },
    descriptionBig: {
        fontSize: 20,
    },
    description: {
        fontSize: 18,
    },
    body: {
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
    section: {
        marginTop: 10,
        marginBottom: 10,
    },
    ratingColumn: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    accordionContainer: {
        backgroundColor: "transparent",
        boxShadow: "none",
        padding: 0,
    },
};

export const CompanyDetails = ({ company }) => {
    const [perksRatings, avgPerksRating] = getPerksRatings(company);
    const [happinessRatings, avgHappinessRatings] =
        getHappinessRatings(company);

    return (
        <div style={styles.container}>
            <div style={styles.section}>
                <Typography style={styles.mainTitle}>{company.name}</Typography>

                <Typography style={styles.description}>
                    Industry: {company.industry}
                </Typography>
            </div>

            <Divider />

            <div style={styles.section}>
                <Collapsable title="Description">
                    <Typography style={styles.body}>
                        {company.description}
                    </Typography>
                </Collapsable>
            </div>

            <Divider />

            <div style={styles.section}>
                <Collapsable title="Ratings">
                    <Grid container>
                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    General
                                </Typography>
                                <RatingComponent
                                    rating={company.custom_rating}
                                    precision={0.1}
                                    title="IndWish"
                                    hasTooltip={true}
                                    tooltipText="This rating is based on the global rating, happiness and perks parameters."
                                />
                                <RatingComponent
                                    rating={company.rating}
                                    precision={0.1}
                                    title="Global"
                                />
                                <RatingComponent
                                    rating={avgHappinessRatings}
                                    precision={0.1}
                                    title="Average Happiness"
                                />
                                <RatingComponent
                                    rating={avgPerksRating}
                                    precision={0.1}
                                    title="Average Perks"
                                />
                            </div>
                        </Grid>

                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Happiness
                                </Typography>

                                {happinessRatings.map((perk) => (
                                    <RatingComponent
                                        rating={perk.rating}
                                        precision={0.1}
                                        title={perk.name}
                                        key={perk.name}
                                    />
                                ))}
                            </div>
                        </Grid>

                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Perks
                                </Typography>

                                {perksRatings.map((perk) => (
                                    <RatingComponent
                                        rating={perk.rating}
                                        precision={0.1}
                                        title={perk.name}
                                        key={perk.name}
                                    />
                                ))}
                            </div>
                        </Grid>
                    </Grid>
                </Collapsable>
            </div>
        </div>
    );
};
