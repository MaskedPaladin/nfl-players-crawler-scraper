# NFL Historic players.

## TODO
> 1. Obtain the html from page: https://www.pro-football-reference.com/players/
> 2. Identify all links with a text letter from a to z.
> 3. Obtain the data from the links obtained from the main page.
> 4. Dump into a csv file.

URLS and accessing labels:
https://www.pro-football-reference.com/players/<letter_to_search>/

INTO THE HTML https://www.pro-football-reference.com/players/:
```html
<ul class="alphabet bullets-inline">
	<li>
		<a href /players/letter>letter</a>
	</li>
	<li>
		<a href /players/letter>letter</a>
	</li>

</ul>
```

INTO THE HTML:
```html
<div id="div_players"> 
<p>
	<a href="LINK_TO_PLAYER_INFO">PLAYER_NAME</a>
</p>
<p>
	<a href="LINK_TO_PLAYER_INFO">PLAYER_NAME</a>
</p>
```

INFO contained in:
```html
<div id="meta">
	<!-- PLAYER_NAME INTO H1 --> 
	<h1>
		<SPAN>PLAYER_NAME<SPAN>
	</h1>
	<!-- player_name into first paragraph -->
	<p> <strong>player_name</strong></p>
	<!-- Position into second paragraph -->
	<p>POSITION</p>
	<!-- Height and weigth into spans inside second paragraph -->
	<p>
		<span itemprop="height">height</span>
		<span itemprop="weight">weight</span>
	</p>
	<!-- birthdate inside span with id necro-birth and itemprop birthDate inside third paragraph, birthplace inside a inside span with itemprop birthPlace-->
	<p>
		<strong>Born:</strong>
		<span id="necro-birth" itemprop="birthDate" data-birth="data_from_birth">data_from_birth</span>
		<nobr>(Aghe: age-d)</nobr>
		<span itemprop="birthPlace">
			<a href="friv/birthplaces.cgi?state=place_of_birth">place_of_birth</a>
		</span>
	</p>
	<!-- College inside a inside fourth paragraph -->
	<p>
		<strong>College</strong>
		<a href="/schools/school">school</a>
	</p>
	<!-- Average inside a inside fifth paragraph -->
	<p>
		<strong>
			<a href="https://www.pro-football-reference.com/blog/indexcd.html?p=page" >AV</a>
		</strong>
		overall
	</p>
	<!-- High school inside a with id high school state inside a witg hs_state inside fifth second paragraph -->
	<p>
		<strong>High School</strong>
		<a href="/schools/high_schools.cgi?id=id">high_school</a>
		<a href="/schools/high_schools.cgi?hs_state=state>state</a>
	</p>
	<!-- Name pronunciation inside a inside sixth paragraph -->
	<p>
		<strong>Pronunciation</pronunciation>
		<a title="Click for all players pronunciations" href="/friv/pronunciation-guide.html">pronunciation</a>
	</p>
</div>
```
- player_name inside first paragraph.
- position inside second paragraph.
- birthdate inside span with id necro-birth and itemprop birthDate inside third paragraph, birthplace inside a inside span with itemprop birthPlace.
- College inside a inside fourth paragraph.
- Average inside a inside fifth paragraph.
- High school inside a with id high school state inside a witg hs_state inside sixth second paragraph.
- Name pronunciation inside a inside seventh paragraph.

