import React from "react";
import { Divider, Grid, Typography } from "@mui/material";
import { RatingComponent } from "./RatingComponent";
import {
    employeeMapper,
    getHappinessRatings,
    getInterviewData,
    getPerksRatings,
    getRolesRatings,
    getRolesSalary,
    revenueMapper,
} from "../utils/utils";
import { Collapsable } from "./Collapsable";
import PaidIcon from "@mui/icons-material/Paid";

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
        fontSize: 16,
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
    mainTitleSection: {
        marginLeft: 15,
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
    salaryItem: {
        fontSize: 18,
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: 5,
    },
};

export const CompanyDetails = ({ company }) => {
    const [perksRatings, avgPerksRating] = getPerksRatings(company);
    const [happinessRatings, avgHappinessRatings] =
        getHappinessRatings(company);
    const [rolesRatings, avgRolesRating] = getRolesRatings(company);
    const [rolesSalary, avgRolesSalary] = getRolesSalary(company);

    const interview = getInterviewData(company);
    const numEmployees = employeeMapper[company.employees];
    const revenue = revenueMapper[company.revenue];

    return (
        <div style={styles.container}>
            <div style={styles.section}>
                <div style={styles.mainTitleSection}>
                    <Typography style={styles.mainTitle}>
                        {company.name}
                    </Typography>

                    <Grid container spacing={2}>
                        <Grid item xs={6}>
                            <Typography style={styles.description}>
                                <b>Industry:</b> {company.industry}
                            </Typography>

                            <Typography style={styles.description}>
                                <b>Headquarters:</b> {company.headquarters}
                            </Typography>
                        </Grid>

                        <Grid item xs={6}>
                            <Typography style={styles.description}>
                                <b>Number of Employees:</b> {numEmployees}
                            </Typography>

                            <Typography style={styles.description}>
                                <b>Revenue:</b> {revenue}
                            </Typography>
                        </Grid>
                    </Grid>
                </div>
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
                <Collapsable
                    title={`Ratings (based on ${company.reviews} reviews)`}
                >
                    <Grid container spacing={2}>
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

            <Divider />

            <div style={styles.section}>
                <Collapsable title="Roles">
                    <Grid container spacing={2}>
                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    General
                                </Typography>

                                <RatingComponent
                                    rating={avgRolesRating}
                                    precision={0.1}
                                    title="Average Roles Rating"
                                />

                                <Typography style={styles.descriptionBig}>
                                    Average Salary:
                                </Typography>
                                <div style={styles.salaryItem}>
                                    {avgRolesSalary ? (
                                        <>
                                            {avgRolesSalary}
                                            <PaidIcon color="success">
                                                {" "}
                                            </PaidIcon>
                                            /h
                                        </>
                                    ) : (
                                        "?"
                                    )}
                                </div>
                            </div>
                        </Grid>

                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Roles
                                </Typography>

                                {rolesRatings.map((perk) => (
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
                                    Salaries
                                </Typography>

                                {rolesSalary.map((perk) => (
                                    <div key={perk.name}>
                                        <Typography style={styles.description}>
                                            {perk.name}:
                                        </Typography>
                                        <div style={styles.salaryItem}>
                                            {perk.salary}
                                            <PaidIcon color="success" />
                                            /h
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </Grid>
                    </Grid>
                </Collapsable>
            </div>

            <Divider />

            <div style={styles.section}>
                <Collapsable title="Interview">
                    <Grid container spacing={2}>
                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Difficulty
                                </Typography>
                                <Typography style={styles.description}>
                                    {interview["difficulty"] ?? "?"}
                                </Typography>
                            </div>
                        </Grid>

                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Experience
                                </Typography>
                                <Typography style={styles.description}>
                                    {interview["experience_"] ?? "?"}
                                </Typography>
                            </div>
                        </Grid>

                        <Grid item xs={4}>
                            <div style={styles.ratingColumn}>
                                <Typography style={styles.titleXS}>
                                    Duration
                                </Typography>
                                <Typography style={styles.description}>
                                    {interview["duration"] ?? "?"}
                                </Typography>
                            </div>
                        </Grid>
                    </Grid>
                </Collapsable>
            </div>
        </div>
    );
};
