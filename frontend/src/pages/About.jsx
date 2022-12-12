import { blue, indigo } from "@mui/material/colors";
import React from "react";

const styles = {
    container: {
        padding: "1rem",
        minHeight: "100vh",
        backgroundColor: "lightBlue",
        boxSizing: "border-box",
        position: "relative",
    },
    centered: {
        display: "flex",
        flex: 1,
        height: "100%",
        alignItems: "center",
        flexDirection: "column",
    },
    title: {
        fontSize: "4rem",
        fontFamily: "Roboto",
    },
    centerColumn: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        height: "100%",
        width: "80%",
        borderRadius: "1rem",
        padding: "2rem",
        border: "solid",
        borderWidth: 2,
        boxSizing: "border-box",
        textAlign: "center",
        fontSize: "1.2rem",
        zIndex: 2,
        backgroundColor: indigo[50],
        boxShadow: "4px 4px 8px 4px rgba(0,0,0,0.2)",
    },
    subTitles: {
        color: blue[900],
        fontFamily: "Roboto",
        margin: 0,
        marginTop: "0.5rem",
    },
};

export const AboutPage = () => {

    return (
        <div style={styles.container}>
            <div style={styles.centered}>
                <h1 style={styles.title}>IndWish</h1>

                <div style={styles.centerColumn}>
                    {/* create a tag with a title for Who we are */}
                    <h2 style={styles.subTitles}>Who we are?</h2>
                    <p>
                        IndWish is a web application targeted for users seeking
                        their dream job. It allows users to search for companies
                        and view their information, from the perspective of
                        their workers. The application was built in the context
                        of the Information Retrieval course at FEUP. Developed
                        by Bruno Rosendo, João Mesquita and Rui Alves, the
                        application aims to provide a simple and intuitive way
                        to search for companies and view their information.
                    </p>

                    <h2 style={styles.subTitles}>How to perform a search?</h2>
                    <p>
                        There are a lot of searches that can be made. The most
                        basic one is simply search for a specific topic, using
                        the default search on the company name, industry and
                        description.
                        <br />
                        The system also supports{" "}
                        <i>
                            wildcards, fuzzying, proximity, range, field
                        </i> and <i>term boosts</i> and more. These querying
                        capabilities are enabled by default, so the Text Input
                        in the Home Page supports them. To become familiar with
                        all the possible queries, we recommend you to visit the{" "}
                        <a href="https://solr.apache.org/guide/6_6/the-standard-query-parser.html">
                            Solr documentation.
                        </a>
                    </p>

                    <h2 style={styles.subTitles}>
                        How to view company's information?
                    </h2>
                    <p>
                        In the results page, after searching, the user has 2
                        columns: one with all the results, and other showing the
                        details of the selected result. The details of the
                        company are shown in the right column of the screen, in
                        a card. To see the details of other company, you simply
                        have to left click on the desired result on the left
                        column and the details will show up on the right.
                    </p>

                    <h2 style={styles.subTitles}>
                        How does the system get the results?
                    </h2>
                    <p>
                        The application is built using React.
                        <br />
                        The data is indexed in Solr and when performing a
                        search, the system retrieves the results provided from
                        Solr and shows them to the user.
                    </p>
                </div>
            </div>
        </div>
    );
};
