import React from "react";
import { IconButton, Typography } from "@mui/material";
import { Check, Delete } from "@mui/icons-material";

const styles = {
    container: {
        padding: "2rem",
    },
    row: {
        display: "flex",
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "center",
        width: "70%",
        backgroundColor: "#f5f5f5",
        marginBottom: "1rem",
        padding: "1rem",
        paddingLeft: "1rem",
        paddingRight: "2rem",
    },
    icon: {
        marginRight: "1rem",
    },
};

/* TODO nº6: Make this component reusable for items in the 'todo' and 'done' state */

export const TodoCard = ({ items, handleDone }) => {
    return (
        <div style={styles.container}>
            {items.map((item) => (
                <div style={styles.row} key={item.id}>
                    <Typography variant="h4">{item.text}</Typography>
                    <div style={styles.icons}>
                        <IconButton
                            color="primary"
                            style={styles.icon}
                            onClick={() => handleDone(item)}
                        >
                            <Check />
                        </IconButton>

                        <IconButton
                            color="error"
                            style={styles.icon}
                            /* TODO nº5: Add method to Delete Todo item (similar to "handleDone") on click */
                        >
                            <Delete />
                        </IconButton>
                    </div>
                </div>
            ))}
        </div>
    );
};
