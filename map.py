import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# ---------------------------------------------------
# CREATE FIGURE
# ---------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 12))

# Background
ax.set_facecolor("#eef2f3")

# ---------------------------------------------------
# DELHI OUTLINE (SIMPLIFIED BASE MAP)
# ---------------------------------------------------

delhi_outline = [
    (1,2), (2,8), (5,10), (9,9),
    (12,7), (13,4), (11,1),
    (7,0), (3,1)
]

outline = Polygon(
    delhi_outline,
    closed=True,
    facecolor="#d9d9d9",
    edgecolor="black",
    linewidth=3,
    alpha=0.4
)

ax.add_patch(outline)

# ---------------------------------------------------
# RENT ZONES
# ---------------------------------------------------

zones = [

    (
        "Dwarka\n₹40k",
        [(1.5,4), (3,4), (3,5.5), (1.5,5.5)],
        "#4CAF50"
    ),

    (
        "Rohini\n₹80k",
        [(2.5,7), (4,7), (4,8.5), (2.5,8.5)],
        "#FF9800"
    ),

    (
        "Janakpuri\n₹1L",
        [(3.5,5), (5,5), (5,6.5), (3.5,6.5)],
        "#FF9800"
    ),

    (
        "Karol Bagh\n₹1.5L",
        [(5,6), (6.5,6), (6.5,7.5), (5,7.5)],
        "#FF9800"
    ),

    (
        "Connaught Place\n₹4L",
        [(6.5,5), (8,5), (8,6.5), (6.5,6.5)],
        "#F44336"
    ),

    (
        "Hauz Khas\n₹5L",
        [(7.5,3), (9,3), (9,4.5), (7.5,4.5)],
        "#F44336"
    ),

    (
        "Greater Kailash\n₹6L",
        [(8.5,2), (10,2), (10,3.5), (8.5,3.5)],
        "#F44336"
    ),

    (
        "Saket\n₹2L",
        [(7,1), (8.5,1), (8.5,2.5), (7,2.5)],
        "#FF9800"
    ),

    (
        "Vasant Kunj\n₹5L",
        [(5.5,1), (7,1), (7,2.5), (5.5,2.5)],
        "#F44336"
    ),

    (
        "Noida\n₹1L",
        [(10.5,4), (12,4), (12,6), (10.5,6)],
        "#FF9800"
    ),

    (
        "Gurgaon\n₹7L",
        [(3,0.5), (6,0.5), (6,1.5), (3,1.5)],
        "#F44336"
    )

]

# ---------------------------------------------------
# DRAW ZONES
# ---------------------------------------------------

for name, coords, color in zones:

    polygon = Polygon(
        coords,
        closed=True,
        facecolor=color,
        edgecolor='white',
        linewidth=2,
        alpha=0.85
    )

    ax.add_patch(polygon)

    # Center labels
    x = sum([p[0] for p in coords]) / len(coords)
    y = sum([p[1] for p in coords]) / len(coords)

    ax.text(
        x,
        y,
        name,
        ha='center',
        va='center',
        fontsize=10,
        weight='bold',
        color='white'
    )

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

plt.title(
    "Delhi Rental Price Zones",
    fontsize=24,
    weight='bold'
)

# ---------------------------------------------------
# REMOVE AXES
# ---------------------------------------------------

ax.set_xticks([])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(0, 14)
ax.set_ylim(0, 11)

# ---------------------------------------------------
# SAVE IMAGE
# ---------------------------------------------------

plt.savefig(
    "delhi_rent_map_final.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("DONE! Saved as delhi_rent_map_final.png")
