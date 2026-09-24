import { CalculateMetadataFunction, Composition } from "remotion";
import { R02Video } from "./R02Video";
import { R03Video } from "./R03Video";
import { R04Video } from "./R04Video";
import { CompleteTourChapter } from "./CompleteTour";
import { TOUR_CHAPTERS } from "./data/complete-tour-production-manifest";

type Props = {};

const calculateMetadata: CalculateMetadataFunction<Props> = () => {
  return {};
};

export const MyComposition = () => {
  return (
    <>
      <Composition id="R02" component={R02Video} durationInFrames={1800} fps={30} width={1920} height={1080} calculateMetadata={calculateMetadata} />
      <Composition id="M07-R03-POC-60S" component={R03Video} durationInFrames={1800} fps={30} width={1920} height={1080} calculateMetadata={calculateMetadata} />
      <Composition id="M07-R04-COMPLETE-TOUR" component={R04Video} durationInFrames={14100} fps={30} width={1920} height={1080} calculateMetadata={calculateMetadata} />
      {TOUR_CHAPTERS.map((chapter) => (
        <Composition
          key={chapter.id}
          id={"M07-" + chapter.id}
          component={CompleteTourChapter}
          durationInFrames={chapter.durationSec * 30}
          fps={30}
          width={1920}
          height={1080}
          defaultProps={{chapterId: chapter.id}}
        />
      ))}
      {TOUR_CHAPTERS.map((chapter) => (
        <Composition
          key={chapter.id + "-S2"}
          id={"M07-S2-" + chapter.id}
          component={CompleteTourChapter}
          durationInFrames={chapter.durationSec * 2}
          fps={2}
          width={1920}
          height={1080}
          defaultProps={{chapterId: chapter.id}}
        />
      ))}
    </>
  );
};
