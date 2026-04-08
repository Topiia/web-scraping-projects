def parse_posts(soup):
    rows = soup.find_all("tr", class_="athing")
    data = []

    for row in rows:
        # rank
        rank_tag = row.find("span", class_="rank")
        rank = int(rank_tag.text.replace(".", "")) if rank_tag else None

        # title + link
        title_tag = row.find("span", class_="titleline")
        title = title_tag.text if title_tag else None
        link = title_tag.a["href"] if title_tag and title_tag.a else None

        # second row (subtext)
        subtext = row.find_next_sibling("tr").find("td", class_="subtext")

        # points
        score_tag = subtext.find("span", class_="score")
        points = int(score_tag.text.replace(" points", "")) if score_tag else 0

        # author
        author_tag = subtext.find("a", class_="hnuser")
        author = author_tag.text if author_tag else None

        # comments
        comments = 0
        links = subtext.find_all("a")
        if links:
            last_link = links[-1].text
            if "comment" in last_link:
                comments = int(last_link.split()[0]) if last_link.split()[0].isdigit() else 0

        data.append({
            "rank": rank,
            "title": title,
            "link": link,
            "points": points,
            "author": author,
            "comments": comments
        })

    return data