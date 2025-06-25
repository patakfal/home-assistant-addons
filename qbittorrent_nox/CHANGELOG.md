# qBittorrent-Nox Add-on Changelog

## v5.1.1-1 – 2025-06-25

<p>qBittorrent v5.1.1 was released.<br />
macOS builds will be available on a later date.<br />
<strong>Builds are currently available only from old trusty SourceForge.</strong> FossHub either locked the account or has login issues. Time will tell.</p>
<details>
Library versions
<table>
  <thead>
    <tr>
      <th scope="col">Library</th>
      <th scope="col">Version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>libtorrent</td>
      <td>1.2.20+git9ab80b8724 / 2.0.11+git2e16847613</td>
    </tr>
    <tr>
      <td>Qt</td>
      <td>6.9.1</td>
    </tr>
    <tr>
      <td>Boost</td>
      <td>1.86 / 1.88</td>
    </tr>
  </tbody>
</table>
</details>
<p>v5.1.1 changelog:</p>
<ul>
<li>BUGFIX: Don't interpret wildcard pattern as filepath globbing (glassez)</li>
<li>BUGFIX: Fix appearance of search history length spinbox (glassez)</li>
<li>BUGFIX: Remove dubious seeding time max value (glassez)</li>
<li>BUGFIX: Fix ratio handling (glassez)</li>
<li>BUGFIX: Fix compilation with Qt 6.6.0 (glassez)</li>
<li>WEBUI: Make General tab text selectable by default (dezza)</li>
<li>WEBUI: Add versioning to local preferences (Chocobo1)</li>
<li>WEBUI: Make multi-rename search & replace fields use a monospace font (Atk)</li>
<li>WEBUI: Fix wrong replacement sequence in IPv6 string (Chocobo1)</li>
<li>WEBUI: Fix memory leak (bolshoytoster)</li>
<li>WEBUI: Fix path autofill in set location and new category (tehcneko)</li>
<li>RSS: Mark matched article as "read" if it refers to a duplicate torrent (glassez)</li>
<li>WINDOWS: Update command line help message (KanishkaHalder1771)</li>
<li>WINDOWS: NSIS: Don't require agreement on the license page (Chocobo1)</li>
<li>LINUX: Fix preview not opening on Wayland (Isak05)</li>
<li>LINUX: Add fallback for random number generator (Chocobo1)</li>
<li><a href="https://github.com/qbittorrent/qBittorrent/compare/release-5.1.0...release-5.1.1">Full changes</a></li>
</ul>


